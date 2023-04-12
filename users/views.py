from django.shortcuts import render
from .forms import UserForm


def register_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    form = UserForm
    data = {
        'form': form
    }
    return render(request, 'users/register.html', data)


def login_page(request):
    # return render(request, 'main/main.html')
    pass
