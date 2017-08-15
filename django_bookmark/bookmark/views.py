from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_page(request):
    output = '''
    <html>
    <head><title>%s</title></head>
    </html>
    <body>
    <h1>%s</h1>
    <p>%s</p>
    </body>
    ''' % (
        'Django Bookmarks',
        'Welcome to django bookmarks',
        'Where you can store bookmakrs',
    )
    return HttpResponse(output)