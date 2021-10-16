"""forumPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler500, url, include
from django.contrib import admin
from django.views.static import serve
from froala_editor import views
from . import views


urlpatterns = [
    path('desponiaAdmin/desponia/admin/', admin.site.urls),
    path('', include("pages.urls")),
    path('user/', include("accounts.urls")),
    path('users/', include("userposts.urls")),
    path('newpost/', include("posts.urls")),
    path('posts/', include("postdetail.urls")),
    path('froala_editor/', include('froala_editor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = views.error400
handler403 = views.error403
handler404 = views.error404
handler500 = views.error500
