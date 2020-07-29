__author__ = "Yuvraj Deshmukh"

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    keys_to_post = ['remove_punctuation', 'uppercase', 'remove_newline', 'remove_extra_space', 'char_count']
    remove_punctuation, uppercase, remove_newline, remove_extra_space, char_count = [request.POST.get(key) for key
                                                                                     in keys_to_post]
    inputText_original = request.POST.get('text', 'default')
    inputText = inputText_original
    result_text = ""

    if remove_punctuation == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in inputText:
            if char not in punctuations:
                analyzed = analyzed + char

        inputText = analyzed
        result_text = 'Punctuations removed\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}

    if uppercase == 'on':
        analyzed = inputText.upper()
        inputText = analyzed
        result_text = result_text + 'Converted to uppercase\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if remove_newline == 'on':
        analyzed = ""
        for char in inputText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        inputText = analyzed
        result_text = result_text + 'Newline removed\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}

    if remove_extra_space == 'on':
        analyzed = ""
        for index, char in enumerate(inputText):
            if not (inputText[index] == " " and inputText[index + 1] == " "):
                analyzed = analyzed + char
        inputText = analyzed
        result_text = result_text + 'Extra space removed\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}

    if char_count == 'on':
        analyzed = analyzed + '\nCharacter count = ' + str(len(inputText_original))
        result_text = result_text + 'Character counted\n'
        params = {'purpose': result_text, 'analyzed_text': analyzed}

    if inputText == "":
        return HttpResponse('Please enter the text and try again.')

    else:
        if remove_punctuation or uppercase or remove_newline or remove_extra_space:
            return render(request, 'analyze.html', params)
        else:
            return HttpResponse('Please select any one operation and try again.....')
