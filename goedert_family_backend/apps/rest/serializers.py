from django.contrib.auth.models import User
from apps.drive.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class RelativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relative
        # fields = ('user','first_name','last_name','birth_date','birth_place','death_date','parents','spouses', 'current_spouse','created_by','created_at','updated_at')
        
        fields = '__all__'

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'