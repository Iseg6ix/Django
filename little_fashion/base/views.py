from django.shortcuts import render


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