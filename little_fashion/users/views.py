from django.shortcuts import render, redirect
from .forms import UserCreationForm


def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get(username)
            email = form.cleaned_data.get(email)
            return redirect('home')
    else:
        form = UserCreationForm()   
    context = {
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'users/sign-up.html', context)

