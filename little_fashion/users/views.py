from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get(username)
            email = form.cleaned_data.get(email)
            return redirect('home')
    else:
        form = SignUpForm()   
    context = {
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'users/form.html', context)


def signin(request):
    context = {
        'title': 'Sign In'
    }
    return render(request, 'users/sign-in.html', context)

