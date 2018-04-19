from django.contrib import admin
from django.urls import include, path, re_path



from . import views


urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^add_relative$', views.add_relative),
    
]