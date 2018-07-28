# views.py ties the url path and the HTML template together

from django.shortcuts import render


def index(request):
    # This is your new view
    return render(request, 'index.html')
