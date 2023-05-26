from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from .forms import RegisterForm, MoneyForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.utils import IntegrityError


@transaction.atomic()
def register_page(request):
    data = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.create_user(email, '', password)
                user.first_name = name
                user.save()
                Customer.objects.create(user=user).save()
                return redirect('/users/login')
            except IntegrityError:
                data['error_message'] = 'Email ' + email + ' has been already used'
        else:
            data['error_message'] = 'Invalid email'

    form = RegisterForm
    data['form'] = form

    return render(request, 'registration/register.html', data)


@login_required
def profile_page(request, message):
    data = {'customer': Customer.objects.get(user=request.user)}
    if message == 'success':
        data['message'] = 'Successfully created your order'
    if message == 'wrong_form':
        data['error_message'] = 'Form was wrong, try again'
    if message == 'not_enough_money':
        data['error_message'] = 'Not enough money'
    if message == 'empty_cart':
        data['error_message'] = 'Can\'t create an order for an empty cart'

    return render(request, 'users/profile.html', data)


@login_required
def pay_page(request):
    data = {}
    if request.method == 'POST':
        form = MoneyForm(request.POST)

        if form.is_valid():
            money = form.cleaned_data.get('money')
            user = Customer.objects.get(user=request.user)
            Customer.objects.filter(id=user.id).update(money=user.money + int(money))
            data['message'] = 'Successfully replenished the balance for ' + str(money)
        else:
            data['error_message'] = 'Form was wrong'

    form = MoneyForm
    data['form'] = form

    return render(request, 'users/pay.html', data)
