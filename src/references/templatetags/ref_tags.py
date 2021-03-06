from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def company_name(prefix):
    return prefix + " " + settings.COMPANY_NAME


