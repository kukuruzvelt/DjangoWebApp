from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.db import transaction


@transaction.atomic()
def catalog(request):
    data = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = request.POST['product_id']
            user = Customer.objects.get(user=request.user)

            product = Product.objects.get(id=product_id)
            if product.quantity > 0:
                Product.objects.filter(id=product_id).update(quantity=product.quantity - 1)
                try:
                    cart_instance = Cart.objects.get(user=user, product=product)
                    Cart.objects.filter(user=user, product=product).update(
                        quantity=cart_instance.quantity + 1)
                except Cart.DoesNotExist:
                    Cart.objects.create(user=user, product=product).save()
                data['message'] = 'Added ' + product.name + ' to cart'
            else:
                data['error_message'] = 'This product is out of stock'
        else:
            data['error_message'] = 'Please log in before adding products to cart'

    # only showing products with quantity > 0
    products = Product.objects.filter(quantity__gt=0)
    data['products'] = products
    return render(request, 'products/catalog.html', data)


@login_required
@transaction.atomic()
def cart(request):
    data = {}

    user = Customer.objects.get(user=request.user)

    if request.method == 'POST':
        # removing item from cart
        product_id = request.POST['prod_id']
        product = Product.objects.get(id=product_id)

        Product.objects.filter(id=product_id).update(quantity=product.quantity + 1)

        cart_instance = Cart.objects.get(user=user, product=product)
        if cart_instance.quantity > 1:
            Cart.objects.filter(user=user, product=product).update(quantity=cart_instance.quantity - 1)
        else:
            Cart.objects.filter(user=user, product=product).delete()

    cart_list = Cart.objects.filter(user=user)
    if cart_list.__len__() > 0:
        data['cart'] = cart_list
        data['total'] = count_total(cart_list)
    else:
        data['message'] = 'Your cart is empty'

    return render(request, 'products/cart.html', data)


@login_required
@transaction.atomic()
def buy(request):
    # todo set up min order date as tomorrow
    data = {}

    user = Customer.objects.get(user=request.user)
    cart_list = Cart.objects.filter(user=user)

    total = count_total(cart_list)
    data['total'] = total

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if cart_list.__len__() < 1:
            message = 'empty_cart'
        elif user.money < total:
            message = 'not_enough_money'
        elif form.is_valid():
            Customer.objects.filter(id=user.id).update(money=user.money - total)
            order = Order.objects.create(user=user, date=form.cleaned_data.get('date'),
                                         city=form.cleaned_data.get('city'))
            order.save()
            for c in cart_list:
                OrderProduct.objects.create(order=order, product=c.product, quantity=c.quantity).save()
                Cart.objects.filter(id=c.id).delete()
            message = 'success'
        else:
            message = 'wrong_form'

        return redirect('/users/profile/' + message)

    form = OrderForm

    data['form'] = form
    data['cart'] = cart_list

    return render(request, 'products/order.html', data)


@login_required
@transaction.atomic()
def orders(request):
    data = {}

    if request.method == 'POST':
        # canceling order
        print(request.POST['order_id'])
        Order.objects.filter(id=request.POST['order_id']).delete()
        data['message'] = 'Successfully deleted your order'

    # todo show cancel button only if order still has not been completed
    order_list = Order.objects.filter(user=Customer.objects.get(user=request.user))
    result = {}
    if order_list.__len__() > 0:
        for o in order_list:
            result[o] = OrderProduct.objects.filter(order=o)
        data['orders'] = result
    else:
        data['error_message'] = 'You have no orders'

    return render(request, 'products/order_list.html', data)


def count_total(cart_list):
    total = 0
    for c in cart_list:
        total += c.product.price * c.quantity
    return total
