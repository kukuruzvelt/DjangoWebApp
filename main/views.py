from django.shortcuts import render, redirect


def main_page(request):
    if request.user.is_authenticated:
        return redirect('/users/profile')
    return render(request, 'main/main.html')
