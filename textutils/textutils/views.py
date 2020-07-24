__author__ = "Yuvraj Deshmukh"

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    #  templates uses
    return render(request, 'index.html')


def remove_punctuation(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # analyze text
    return HttpResponse("remove_punctuation")


def capitalize_first(request):
    return HttpResponse("capitalize_first")


def remove_newline(request):
    return HttpResponse("remove_newline")


def remove_space(request):
    return HttpResponse("remove_space")


def char_count(request):
    return HttpResponse("char_count")

