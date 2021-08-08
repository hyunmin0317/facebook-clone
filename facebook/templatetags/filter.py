from django import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from common.models import Profile
from facebook.models import Post

register = template.Library()

@register.simple_tag
def confirm(username, fusername):
    user = get_object_or_404(User, username=username)
    fuser = get_object_or_404(User, username=fusername)
    profile = get_object_or_404(Profile, user=fuser)
    if(user in profile.follow.all()):
        return 'follow'
    return 'unfollow'

@register.simple_tag
def confirm_like(username, post_id):
    try:
        user = User.objects.get(username=username)
        post = get_object_or_404(Post, id=post_id)
        if (user in post.voter.all()):
            return 'like'
        return 'unlike'
    except:
        return 'unlike'