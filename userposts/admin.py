from django.contrib import admin
from .models import UserPosts,UserMessages

class postAdmin(admin.ModelAdmin):
    list_display=("id","username","category","created_at",)
    list_display_links = ('id',"username")

admin.site.register(UserPosts,postAdmin)

class messageAdmin(admin.ModelAdmin):
    list_display=("id","username","created_at",)
    list_display_links = ('id',"username")

admin.site.register(UserMessages,messageAdmin)

