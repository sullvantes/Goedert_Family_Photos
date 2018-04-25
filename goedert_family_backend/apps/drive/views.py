from django.shortcuts import render
from rest_framework import viewsets

from quickstart import * 
from .models import *



# Create your views here.

def home(request):
    # all_pics = ['1I1xjr_unaA2H1_LfB4Nqyk7nbQVryWI4']
    all_pics = get_last10()
    for pic in all_pics:
        print (pic['name'], pic['id'])
    response = {
        'pictures' : all_pics 
        }    
    return render(request, "drive/home.html",response)

def add_relative(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RelativeForm()
    
    response = {
        'form' : form 
        }    
    return render(request, "drive/add_relative.html", response)
