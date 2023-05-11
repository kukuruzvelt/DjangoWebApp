from django.shortcuts import render
from .models import Product, Cart


# Create your views here.
def catalog(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = request.POST['product_id']
            user_id = request.user.id
            print(product_id, user_id)
            cart_instance = Cart.objects.create(user_id=user_id, product_id=product_id)
            cart_instance.save()
        else:
            print('Not logged in')
            pass

    products = Product.objects.all()
    data = {'products': products}
    return render(request, 'products/catalog.html', data)


def cart(request):
    data = {}
    products = []
    if request.user.is_authenticated:
        items = Cart.objects.filter(user_id=request.user.id)
        for item in items:
            products.append(Product.objects.get(id=item.id))
        if not products:
            data['message'] = 'Your cart is empty'
        else:
            data['products'] = products
    else:
        data['error_message'] = 'Log in before seeing your cart'
    return render(request, 'products/cart.html', data)
