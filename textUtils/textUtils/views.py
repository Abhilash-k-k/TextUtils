#I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Home Text')
    return render(request, 'index.html')

def removepunc(request):
    #Get teh text
    djtextrecived = request.POST.get('text', 'default')

    #Check which checkbox is checked
    puncselect = request.POST.get('removepunc', 'off')
    capitselect = request.POST.get('capitalise', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analysed_text = ''

    if puncselect == 'on':
        punc_list='''!()-[]{};:'"\/,<>.?@$%^&*_-'''
        for i in djtextrecived:
            if i not in punc_list:
                analysed_text += i
        params = {'purpose': 'Remove punctuations', 'analyzed_text': analysed_text}
        djtextrecived = analysed_text
    if capitselect == 'on':
        for i in djtextrecived:
            analysed_text += i.upper()
        params = {'purpose': 'Capitalise', 'analyzed_text': analysed_text}
        djtextrecived = analysed_text
    if newlineremover == 'on':
        for i in djtextrecived:
            if i != '\n' or i != '\r':
                analysed_text += i

        params = {'purpose': 'NewLinerRemover', 'analyzed_text': analysed_text}
        djtextrecived = analysed_text
    if extraspaceremover == 'on':
        for index, char in enumerate(djtextrecived):
            if not(djtextrecived[index] == ' ' and djtextrecived[index+1] == ' '):
                analysed_text += char
        params = {'purpose': 'ExtraSapceRemover', 'analyzed_text': analysed_text}
        djtextrecived = analysed_text
    if charcount == 'on':
        count = 0
        for i in djtextrecived:
            count += 1
        analysed_text = f'{analysed_text} and the count is {count}'
        params = {'purpose': 'Char counter', 'analyzed_text': analysed_text}
    if (puncselect != 'on' and capitselect != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse('Please select any of the options and then retry')
    else:
        return render(request, 'analyze.html', params)


def capitalisefirst(request):
    return HttpResponse('capitalisefirst')

def newlineremove(request):
    return HttpResponse('newlineremove')

def spaceremove(request):
    return HttpResponse('spaceremove')

def charcount(request):
    return HttpResponse('charcount')