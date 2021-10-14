from django.urls import path
from . import views

urlpatterns = [
    path('<int:_detail>',views.detail_post, name="detail"),
    path('like/<int:pk>',views.liked_post, name="like_post"),
    path('like-message/<int:pk>',views.liked_message, name="like_message"),
    path('<int:pk>/edit',views.PostUpdateView.as_view(), name="post-update"),
    path('<int:pk>/delete',views.PostDeleteView.as_view(), name="post-delete"),
    path('<int:pk>/message/edit',views.MessageUpdateView.as_view(), name="message-update"),
    path('<int:pk>/message/delete',views.MessageDeleteView.as_view(), name="message-delete"),
    path('reply/<int:pk>',views.reply, name="reply-message"),
]
