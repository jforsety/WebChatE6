from .views import ApiProfile, ApiChatRoom
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from . import views


router = DefaultRouter()
router.register('rooms', ApiChatRoom)
router.register('user', ApiProfile)

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('api/', include(router.urls)),
]