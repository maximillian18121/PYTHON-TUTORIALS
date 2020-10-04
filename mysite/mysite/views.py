from django.http import HttpResponse
from django.shortcuts import render

def indexes(request):
    return render(request, 'index.html')
def analyze(request):
    data = request.GET.get("text", "default")
    data1 = request.GET.get("analyze", "off")
    data2 = request.GET.get("fullcaps", "off")
    data3 = request.GET.get("newlineremover", "off")
    data4 = request.GET.get("spaceremover", "off")
    data5 = request.GET.get("charcounter", "off")

    analyzed = ""
    punctuations = '''()[]{}<>@#$%^&*(){}[]:;"/?.,+=_-'^'''
    space = " "
    if data1 == 'on':
        for char in data:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {
                    'function': ' REMOVE PUNCTUATIONS ',
                    'des': analyzed,
                }
        data = analyzed

    elif data2 == 'on':
        for char in data:
            if char not in punctuations:
                analyzed = analyzed + char.upper()

        param = {
                    'function': ' CAPITALIZE CHARACTERS ',
                    'des': analyzed,
                }
        data = analyzed

    elif data3 == 'on':
        for char in data:
            if char != "\n":
                analyzed = analyzed + char

        param = {
                    'function': ' REMOVE NEWLINE ',
                    'des': analyzed,
                }
        data = analyzed

    elif data4 == 'on':
        for char in data:
            if char not in space:
                analyzed = analyzed + char

        param = {
                    'function': ' REMOVE SPACE ',
                    'des': analyzed,
                }
        data = analyzed

    elif data5 == 'on':
        sum = 0
        for index, char in enumerate(data):

            sum = index+sum
            analyzed = sum

        param = {
            'function': ' COUNT CHARACTERS ',
            'des': analyzed,
        }
        data = analyzed

    else:
        return HttpResponse("ERROR 404")

    return render(request, 'analyze.html', param)




#def capfirst(request):
   # return HttpResponse('''<h1>CAPITALIZE THE FIRST LETTER</h1>
    #<a href="/">GO TO HOME</a>''')
#def newlinerremove(request):
   # return HttpResponse('''<h1>REMOVE THE NEWLINE TAG</h1>
    #<a href="/">GO TO HOME</a>''')
#def spaceremove(request):
   # return HttpResponse('''<h1>REMOVE THE SPACE</h1>
   # <a href="/">GO TO HOME</a>''')
#def charcount(request):
  #  return HttpResponse('''<h1>COUNT THE CHARACTERS</h1>
   # <a href="/">GO TO HOME</a>''')


