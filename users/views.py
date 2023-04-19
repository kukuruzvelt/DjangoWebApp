from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User


def register_page(request):
    # todo add error message if form isn't valid
    # todo add password encoding
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['login'], '', form.cleaned_data['password'])

            user.first_name = form.cleaned_data['name']
            user.save()
            form.save()
            return redirect('/users/login')

    form = UserForm
    data = {
        'form': form
    }
    return render(request, 'registration/register.html', data)
