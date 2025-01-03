from django import template
from accounts.models import Notifications

register = template.Library()

@register.inclusion_tag('accounts/show_notifications.html', takes_context=True)
def show_notifications(context):
	request_user = context['request'].user
	notifications = Notifications.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date')
	return {'notifications': notifications}