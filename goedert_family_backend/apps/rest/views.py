from django.contrib.auth.models import User
from apps.drive.models import *
from rest_framework import viewsets
from apps.rest.serializers import UserSerializer, RelativeSerializer, PhotoSerializer, NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class RelativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Relative.objects.all()
    serializer_class = RelativeSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer