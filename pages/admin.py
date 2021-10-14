from django.contrib import admin
from .models import Report, Setting, ContactUs
# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id","report")
    list_display_links = ("id","report")
admin.site.register(Report,ReportAdmin)
admin.site.register(Setting)
admin.site.register(ContactUs)