from django import template

register = template.Library()

@register.filter(name="multiply")
def multiply(a, b):
    """Multiplies two values."""
    return a * b

