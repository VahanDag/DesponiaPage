from django.urls import path
from . import views

urlpatterns = [
    path('<str:userName>',views.users, name="users"),
]
