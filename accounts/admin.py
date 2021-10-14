from django.contrib import admin
from .models import Notifications, Profile, UserRanks
# Register your models here.

admin.site.register(Profile)

class UserRanksAdmin(admin.ModelAdmin):
    list_display= ('id','user')
    list_display_links = ('id','user')

admin.site.register(UserRanks,UserRanksAdmin)

admin.site.register(Notifications)