from django import template
register = template.Library()

@register.filter
def title(value, key):
	ss=str(key)
	return value[ss][0]

@register.filter
def link(value, key):
	ss=str(key)
	return value[ss][1]

@register.filter
def image(value, key):
	ss=str(key)
	return value[ss][2]