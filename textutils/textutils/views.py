__author__ = "Yuvraj Deshmukh"

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    #  templates uses
    return render(request, 'index.html')


# def remove_punctuation(request):
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # analyze text
#     return HttpResponse("remove_punctuation")
#
#
# def capitalize_first(request):
#     return HttpResponse("capitalize_first")
#
#
# def remove_newline(request):
#     return HttpResponse("remove_newline")
#
#
# def remove_space(request):
#     return HttpResponse("remove_space")
#
#
# def char_count(request):
#     return HttpResponse("char_count")

def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    remove_punc = request.GET.get('removepunctuation', 'default')
    print(remove_punc)

    if (remove_punc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

    # analyze text
    # return HttpResponse("remove_punctuation")
