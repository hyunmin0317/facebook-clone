from django import template

register = template.Library()

@register.filter
def confirm(user, follow):
    if(user in follow):
        return 'unfollow'
    return 'follow'