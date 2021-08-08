from django import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from common.models import Profile

register = template.Library()

@register.simple_tag
def confirm(username, fusername):
    user = get_object_or_404(User, username=username)
    fuser = get_object_or_404(User, username=fusername)
    profile = get_object_or_404(Profile, user=fuser)
    if(user in profile.follow.all()):
        return 'follow'
    return 'unfollow'