from django import template

register = template.Library()

@register.filter(name='restar')
def restar(value, arg):
    return value - arg
