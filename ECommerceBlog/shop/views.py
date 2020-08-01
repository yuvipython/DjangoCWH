from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


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
