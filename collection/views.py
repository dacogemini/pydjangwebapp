# views.py ties the url path and the HTML template together

from django.shortcuts import render


def index(request):
    # Define a variable here: 
    # Passing the variable through the view:
    return render(request, 'index.html', {
    })
