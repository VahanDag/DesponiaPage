from django.db import models
from accounts.models import UserMessages, UserPosts
from django.contrib.auth.models import User

class Report(models.Model):
    to_user = models.ForeignKey(User, related_name='report_to', on_delete=models.CASCADE, null=True,blank=True)
    report = models.CharField(max_length=200, blank=True, null=True, verbose_name='Report Reason',)
    from_user = models.ForeignKey(User, related_name="report_from", on_delete=models.CASCADE, null=True,blank=True)
    post = models.ForeignKey(UserPosts, related_name="+", blank=True,null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(UserMessages, related_name="+", blank=True, null=True, on_delete=models.CASCADE)


class Setting(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=200, default="light.css")

	def __str__(self):
		return self.name

class ContactUs(models.Model):
    email = models.CharField(max_length=200)
    content = models.TextField(max_length=600)

    def __str__(self):
        return self.email