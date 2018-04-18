from django.db import models
from django.forms import ModelForm

# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.contrib import admin
# from django.forms import ModelForm

class Relative(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL, related_name = 'related_relative')
    first_name= models.CharField(max_length = 50, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last Name')
    birth_date = models.DateField(null = True, blank = True)
    birth_place = models.CharField(max_length = 50, null = True, blank = True, verbose_name = 'Birthplace')
    death_date= models.DateField(null = True, blank = True)
    parents = models.ManyToManyField("self", blank=True)
    spouses = models.ManyToManyField("self", blank=True)
    current_spouse = models.ForeignKey("self", null = True, blank = True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL, related_name = 'created_relatives')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    class Meta:
        ordering = ['last_name', 'first_name']
    
    def display_name(self):
        if self.last_name:
            if self.first_name:
                return "%s, %s" % (self.last_name_1, self.first_name_1)
            else:
                return "%s" % self.last_name
        else:
            return "%s" % self.first_name

    def __unicode__(self):
        return self.first_name, self.last_name

class RelativeForm(ModelForm):
    class Meta:
        model = Relative
        fields = '__all__'

class Photo(models.Model):
    drive_id = models.CharField(max_length = 50)
    drive_title = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    year = models.DateField(null = True, blank = True)
    relatives = models.ManyToManyField(Relative, related_name = "photos")
    # tags = models.ManyToManyField(Tag,related_name='photos')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.drive_title

class Note(models.Model):
    created_by = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL, related_name = 'users_notes')
    photo = models.ForeignKey(Photo, null = True, blank = True, on_delete=models.CASCADE, related_name = 'photos_notes' )
    note = models.TextField(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)