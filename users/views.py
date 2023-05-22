from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.db import transaction


@transaction.atomic()
def register_page(request):
    data = {}
    if request.method == 'POST':
        login = request.POST['login']
        name = request.POST['name']
        password = request.POST['password']
        # todo ensure that fields are valid, add error to data{} if not
        user = User.objects.create_user(login, '', password)
        user.first_name = name
        user.save()

        Customer.objects.create(user=user).save()

        return redirect('/users/login')

    return render(request, 'registration/register.html', data)


@login_required
def profile_page(request):
    data = {'customer': Customer.objects.get(user=request.user)}
    return render(request, 'users/profile.html', data)


@login_required
def pay_page(request):
    data = {}
    if request.method == 'POST':
        # todo validate money field
        money = request.POST['money']
        user = Customer.objects.get(user=request.user)
        Customer.objects.filter(id=user.id).update(money=user.money + int(money))
        data['message'] = 'Successfully replenished the balance for ' + money

    return render(request, 'users/pay.html', data)
