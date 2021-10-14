from django.urls import path
from . import views
from .views import newPost

urlpatterns = [
    path('<str:ctgUrl>',newPost, name="newpost"),
]
