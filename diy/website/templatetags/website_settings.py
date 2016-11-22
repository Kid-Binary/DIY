# diy_project/diy/website/templatetags/website_settings.py
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_socials():
    return settings.SOCIALS