from django import template

register = template.Library()

@register.filter
def space_number(value): # Only one argument.
    num1 = value[0:3]
    num2 = value[3:6]
    num3 = value[6:11]

    return f'{num1} {num2} {num3}'