from django import template

register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)

# @register.filter(name='python_all')
# def python_all(x):
#     return all(x)