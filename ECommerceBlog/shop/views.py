from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse('contact Us')
    # return render(request, 'shop/index.html')


def tracker(request):
    return HttpResponse('tracker')
    # return render(request, 'shop/index.html')


def search(request):
    return HttpResponse('search')
    # return render(request, 'shop/index.html')


def productview(request):
    return HttpResponse('productview')
    # return render(request, 'shop/index.html')


def checkout(request):
    return HttpResponse('checkout')
    # return render(request, 'shop/index.html')
