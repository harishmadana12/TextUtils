# I have made this file -- Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    var = {'name': 'Harry', 'place': 'India'}
    return render(request, 'index.html', var)


def analyzer(request):
    # Get the text
    tex = request.POST.get('text', 'default')
    # check checkbox name from index.html
    removepunc = request.POST.get('removepunc', 'off')
    capitalchar = request.POST.get('capitalchar', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    params = ""
    # checking the condition
    if removepunc == "on":
        punc = '''!@#$%^&*()-[]:;"',_<>'''
        analyzed = ""
        for char in tex:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        tex = analyzed

    if capitalchar == "on":
        analyzed = ""
        for char in tex:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Upper', 'analyzed_text': analyzed}
        tex = analyzed

    if newlinerem == "on":
        analyzed = ""
        for char in tex:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLine', 'analyzed_text': analyzed}
        tex = analyzed

    if removepunc != "on" and newlinerem != "on" and capitalchar != "on" :
        params = {'purpose': 'Look at checkbox', 'analyzed_text': 'Error'}
        return render(request, 'analysed.html', params)

    return render(request, 'analysed.html', params)  # It helps to run multiple checkbox


def about(request):
    return HttpResponse("<h2>About Harry</h2>")


def spaceremove(request):
    return HttpResponse("space remover <a href='/'>Back</a>")
