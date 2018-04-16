from django.db import models

# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.contrib import admin
# from django.forms import ModelForm

class Relative(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL)
    first_name= models.CharField(max_length = 50, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last Name')
    birth_date = models.DateField(null = True, blank = True)
    birth_place = models.CharField(max_length = 50, verbose_name = 'Last Name')
    death_date= models.DateField(null = True, blank = True)
    parents = models.ManyToManyField("self", blank=True)
    spouses = models.ManyToManyField("self", blank=True)
    current_spouse = models.ForeignKey("self", null = True, blank = True, on_delete=models.SET_NULL)
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
        return self.display_name

class ArticleForm(ModelForm):
    class Meta:
        model = Article

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

class Notes(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, null = True, blank = True, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)