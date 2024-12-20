from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return int(value) - int(arg)

@register.filter
def multiply(value, arg):
    return int(value) * int(arg)

@register.filter
def modulo(value, arg):
    return int(value) % int(arg) 