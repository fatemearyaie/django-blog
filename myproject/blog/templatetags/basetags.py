from django import template
from ..models import category

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ من"

@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        "category" : category.objects.filter(status=True)
    }

@register.inclusion_tag("registeration/partials/link.html")
def link(request, link_name, content):
    return {
        "request" : request,
        "content" : content,
        "link_name" : link_name,
        "link" : "blog:{}".format(link_name),
    }