from django.shortcuts import render
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
    else:
        data['message'] = 'Your cart is empty'

    return render(request, 'products/cart.html', data)


@login_required
@transaction.atomic()
def buy(request):
    # todo error if not enough money to buy and redirect back to cart
    data = {}

    user = Customer.objects.get(user=request.user)
    products = get_products_for_user(user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=user, date=form.cleaned_data.get('date'),
                                         city=form.cleaned_data.get('city'))
            order.save()
            for prod in products:
                OrderProduct.objects.create(order=order, product=prod).save()
                Cart.objects.filter(user=user, product=prod).delete()
                # todo redirect to profile with message about successful order creation
        else:
            data['error_message'] = 'Form was wrong, try again'

    form = OrderForm

    data['form'] = form

    return render(request, 'products/order.html', data)


def get_products_for_user(user):
    products = []
    items = Cart.objects.filter(user=user)
    for item in items:
        products.append(item.product)
    return products
