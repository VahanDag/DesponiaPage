from django.contrib import admin
from .models import Category



class CategoryAdmin(admin.ModelAdmin):
    list_display= ('id','categoryName','totalPost','totalMessage')
    list_display_links = ('id','categoryName')

admin.site.register(Category,CategoryAdmin)