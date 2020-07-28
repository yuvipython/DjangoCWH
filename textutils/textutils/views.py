__author__ = "Yuvraj Deshmukh"

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    #  templates uses
    return render(request, 'index.html')


def analyze(request):
    keys_to_get = ['remove_punctuation', 'uppercase', 'remove_newline', 'remove_extra_space', 'char_count']
    remove_punctuation, uppercase, remove_newline, remove_extra_space, char_count = [request.GET.get(key) for key
    in keys_to_get]
    djtext = request.GET.get('text', 'default')
    result_text = ""
    # remove_punctuation = request.GET.get('remove_punctuation', 'default')
    # uppercase = request.GET.get('uppercase', 'default')
    # remove_newline = request.GET.get('remove_newline', 'default')
    # remove_extra_space = request.GET.get('remove_extra_space', 'default')
    # char_count = request.GET.get('char_count', 'default')
    # djlist = request.GET.getlist('remove_punctuation', 'uppercase', 'remove_newline')
    # print(djlist)
    # print(remove_punctuation)

    if remove_punctuation == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        djtext = analyzed
        result_text = 'Punctuations removed\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}

        # return render(request, 'analyze.html', params)

    if uppercase == 'on':
        analyzed = djtext.upper()
        djtext = analyzed
        result_text = result_text + 'text converted to Uppercase\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if remove_newline == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        djtext = analyzed
        result_text = result_text + 'Newline removed\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if remove_extra_space == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        result_text = result_text + 'Extra Space Removed\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if char_count == 'on':
        analyzed = analyzed + '\nCharacter count = '+str(len(djtext))
        # for index, char in enumerate(djtext):
        #     if not (djtext[index] == " " and djtext[index+1] == " "):
        #         analyzed = analyzed + char
        # analyzed = analyzed
        result_text = result_text + 'Character Count\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)

    if remove_punctuation or uppercase or remove_newline or remove_extra_space:
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
