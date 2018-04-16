from django.db import models

# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.contrib import admin
# from django.forms import ModelForm

# class Relative(models.Model):
#     user = models.ForeignKey(Neighborhood, null = True, blank = True)
#     full_name = models.CharField(max_length=50, unique = True)
#     birth_date = models.DateField(null = True, blank = True)
death_date= models.DateField(null = True, blank = True)
#     class Meta:
#         ordering = ['full_name']
    
#     def __str__(self):
#         return self.full_name

    
# class Client(models.Model):
#     phone_types = (('C', 'Mobile'),
#                    ('H', 'Home'),
#                    ('W', 'Work'),
#                    ('F', 'Fax'),
#                    ('O', 'Office')
#                    )

#     code_types = (('G' , 'Garage'), ('D', 'Door'), ('A', 'Alarm'))
    
    
#     payment_types = (('CC', 'Credit Card'), ('CH', 'Check'), ('CA', 'Cash'), ('PP', 'PayPal'))
    
#     first_name_1 = models.CharField(max_length = 255, verbose_name = 'First Name')
#     last_name_1 = models.CharField(max_length = 255, verbose_name = 'Last Name')
#     first_name_2 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = '2nd First Name')
#     last_name_2 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = '2nd Last Name')
#     phone_1 = models.CharField(max_length = 255, verbose_name = 'Phone1')
#     phone_type_1 =models.CharField(max_length = 1, choices = phone_types, null = True, blank = True)
#     phone_2 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Phone2')
#     phone_type_2 =models.CharField(max_length = 1, choices = phone_types, null = True, blank = True)
#     phone_3 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Phone3')
#     phone_type_3 =models.CharField(max_length = 1, choices = phone_types, null = True, blank = True)
#     phone_4 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Phone4')
#     phone_type_4 =models.CharField(max_length = 1, choices = phone_types, null = True, blank = True)
#     email_1 = models.EmailField(verbose_name = 'Email')
#     email_2 = models.EmailField(null=True, blank = True, verbose_name = 'CCEmail')
#     address = models.CharField(max_length = 255)
#     city = models.CharField(max_length = 45)
#     state = models.CharField(max_length = 45)
#     zip_code = models.CharField(max_length = 10)
#     neighborhood = models.ForeignKey(Neighborhood, null = True, blank = True)
#     payment_old =  models.CharField(max_length = 2, choices = payment_types, null = True, blank = True, verbose_name = 'Payment_String')
#     rate = models.FloatField(null=True)
#     rate_str = models.CharField(max_length = 50, null = True, blank = True, verbose_name = 'Rate_String')
#     rate_wknd = models.FloatField(default = 25.0)
    
#     note = models.TextField(null = True, blank = True)
#     leash_loc = models.CharField(max_length = 50, null = True, blank = True, verbose_name = 'Leash Location')
#     notepad_loc = models.CharField(max_length = 50, null = True, blank = True, verbose_name = 'Notepad Location')
#     treats_loc = models.CharField(max_length = 50, null = True, blank = True, verbose_name = 'Treats Location')
#     waterbowl_loc = models.CharField(max_length = 50, null = True, blank = True, verbose_name = 'Waterbowl Location')
#     crate_loc = models.CharField(max_length = 50, null = True, blank = True, verbose_name = 'Crate Location')
#     code_1 = models.CharField(max_length = 50, null = True, blank = True)
#     code_type_1 = models.CharField(max_length = 1, choices = code_types, null = True, blank = True)
#     code_2 = models.CharField(max_length = 50, null = True, blank = True)
#     code_type_2 = models.CharField(max_length = 1, choices = code_types, null = True, blank = True)
#     code_3 = models.CharField(max_length = 50, null = True, blank = True)
#     code_type_3 = models.CharField(max_length = 1, choices = code_types, null = True, blank = True)
    
#     referred_by =  models.CharField(max_length = 50, null = True, blank = True)
#     terminated = models.BooleanField(default = False)
#     terminated_since = models.DateField(null = True, blank = True)
#     terminated_since_str = models.CharField(max_length = 50, null = True, blank = True)
#     terminated_reason = models.TextField(null = True, blank = True)
#     keys = models.CharField(max_length = 50, null = True, blank = True)
#     keys_received = models.BooleanField(default = False)
#     keys_received_str = models.CharField(max_length = 50, null = True, blank = True)
#     start_date = models.DateTimeField(null=True)
#     start_date_str = models.CharField(max_length = 50, null = True, blank = True)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     class Meta:
#         ordering = ['last_name_1','first_name_1']

#     def __str__(self):
#         return self.display_name().title()

#     def display_name(self):
        
#         if self.last_name_1:
#             if self.first_name_1:
#                 return "%s, %s" % (self.last_name_1, self.first_name_1)
#             else:
#                 return "%s" % self.last_name_1
#         else:
#             return "%s" % self.first_name_1
    
#     # def all_notes(self):


# class ClientForm_New(ModelForm):
#     class Meta:
#         model = Client
#         fields = '__all__'
#         # fields = ['first_name_1','last_name_1,''first_name_2','last_name_2','phone_1','phone_type_1','phone_2','phone_type_2','phone_3','phone_type_3','phone_4','phone_type_4','email_1','email_2','address','city','state','zip_code','neighborhood','payment_old','rate','rate_str','note','leash_loc','notepad_loc','treats_loc','waterbowl_loc','crate_loc','code_1','code_type_1','code_2','code_type_2','code_3','code_type_3','referred_by','terminated','terminated_since','terminated_since_str','terminated_reason','keys','keys_received','keys_received_str','start_date','start_date_str']

# class ClientForm_Old(ModelForm):
#     class Meta:
#         model = Client
#         # fields = '__all__'
#         fields = ['first_name_1','last_name_1','first_name_2','last_name_2','phone_1','phone_2','phone_3','phone_4','email_1','email_2','address','city','state','zip_code','start_date_str','keys_received_str','payment_old','rate_str','referred_by','terminated_since_str','terminated_reason','keys','note']


# class Dog(models.Model):
#     name = models.CharField(max_length = 50)
#     owner = models.ForeignKey(Client, related_name = 'dogs')
#     note = models.CharField(max_length = 500, null = True, blank = True)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     def __str__(self):
#         return self.name.title()


# class Walker(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     client = models.ManyToManyField(Client, through="WalkerClientRelationship", related_name = "Walkers")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     walk_rate=models.FloatField(default=7.00)
#     additional_dog_rate=models.FloatField(default=2.00)
#     transportation_reimbursement= models.FloatField(default=0.00)
    
#     neighborhoods=models.ManyToManyField(Neighborhood, related_name = "Walkers")

#     class Meta:
#         ordering = ['user__last_name', 'user__first_name']

#     def __str__(self):
#         return self.display_name().title()

#     def display_name(self):
#         if self.user.last_name or self.user.last_name == 'X':
#             if self.user.first_name:
#                 return "%s, %s" % (self.user.last_name, self.user.first_name.title())
#             else:
#                 return "%s" % self.user.last_name
#         else:
#             return "%s" % self.user.first_name


# class WalkerClientRelationship(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     walker = models.ForeignKey(Walker, on_delete=models.CASCADE)
#     current = models.BooleanField(default = True)
#     walking_since = models.DateField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     disallowed = models.BooleanField(default = False) 
#     disallowed_reason = models.CharField(max_length=255, null = True, blank = True)
#     disallowed_date = models.DateField(null = True, blank = True)

#     def __str__(self):
#         return "%s/%s" % (self.walker.user.last_name, self.client.last_name_1)

# class Update(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
#     change = models.TextField()
#     created_at = models.DateTimeField(auto_now_add = True)
    
#     def __str__(self):
#         return self.change