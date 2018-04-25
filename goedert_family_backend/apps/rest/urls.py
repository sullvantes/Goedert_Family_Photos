from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers


from . import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'relatives', views.RelativeViewSet)
router.register(r'photos', views.PhotoViewSet)
router.register(r'notes', views.NoteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]