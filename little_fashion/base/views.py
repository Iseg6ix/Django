from django.shortcuts import render
from users.forms import ContactForm


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'base/index.html', context)

def products(request):
    context = {
        'title': 'Products'
    }
    return render(request, 'base/products.html', context)



def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'base/about.html', context)


def contact(request):
    form = ContactForm()
    context = {
        'title': 'contact',
        'form': form
    }
    return render(request, 'base/contact.html', context)


def faq(request):
    context = {
        'title': 'faq'
    }
    return render(request, 'base/faq.html', context)