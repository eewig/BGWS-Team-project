from django import template
from ..models import Like


register = template.Library()


@register.filter
def countlikes(post):
	return Like.objects.filter(post=post, liked=True).count()


@register.filter
def isliked(post, user):
	if user.is_anonymous:
		return False
	return bool(Like.objects.filter(post=post, user=user, liked=True))
