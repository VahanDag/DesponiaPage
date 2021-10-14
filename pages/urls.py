from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('forums/<str:forumname>',views.forums,name="forums"),
    path('hierarchy',views.hierarchy,name="hierarchy"),
    path('reports/message/<int:id>',views.reportsMessage, name="report-message"),
    path('reports/post/<int:id>',views.reportPost, name="report-post"),
    path('notification/<int:notifications_pk>/post/<int:userposts_pk>', views.PostNotification.as_view(), name='post-notification'),
	path('user_settings/', views.userSettings, name="user_settings"),
	path('update_theme/', views.updateTheme, name="update_theme"),
	path('categories/', views.categories, name="categories"),
	path('about-us/', views.aboutUs, name="about"),
	path('term-of-service/', views.termofservices, name="tos"),
	path('privacy/', views.privacy, name="privacy"),
	path('contact/', views.contact, name="contact"),
]
