from django import template
register = template.Library()

@register.simple_tag
def title(value,cnt, key):
	sc=str((cnt+1)*4+key)
	return value[sc][0]

@register.simple_tag
def link(value,cnt, key):
	sc=str((cnt+1)*4+key)
	return value[sc][1]

@register.simple_tag
def image(value,cnt, key):
	sc=str((cnt+1)*4+key)
	return value[sc][2]