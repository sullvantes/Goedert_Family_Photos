from django.shortcuts import render
from quickstart import * 

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
