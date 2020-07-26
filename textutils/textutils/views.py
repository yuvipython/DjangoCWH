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
    remove_punctuation = request.GET.get('remove_punctuation', 'default')
    uppercase = request.GET.get('uppercase', 'default')
    remove_newline = request.GET.get('remove_newline', 'default')
    remove_extra_space = request.GET.get('remove_extra_space', 'default')
    char_count = request.GET.get('char_count', 'default')


    print(remove_punctuation)

    if remove_punctuation == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif uppercase == 'on':

        analyzed = djtext.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif remove_newline == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif remove_extra_space == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif char_count == 'on':
        analyzed = djtext
        # for index, char in enumerate(djtext):
        #     if not (djtext[index] == " " and djtext[index+1] == " "):
        #         analyzed = analyzed + char

        params = {'purpose': 'Remove Extra Space', 'analyzed_text': len(analyzed)}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

    # analyze text
    # return HttpResponse("remove_punctuation")


# Example 1

def e1(request):
    returnString = '''<h1>Entertainment : </h1><a href = https://www.google.com>Sab Milega</a>
    <h1>Social Media : </h1><a href = https://www.facebook.com>Facebook</a>'''
    return HttpResponse(returnString)
