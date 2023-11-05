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



def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'base/about.html', context)


def contact(request):
    context = {
        'title': 'contact'
    }
    return render(request, 'base/contact.html', context)