# coding=utf-8
from django import template
from django.utils.http import urlquote_plus

register = template.Library()


@register.filter
def urlfy(value):
    return urlquote_plus(value)
