from django import template
from django.urls import resolve
from django.utils.safestring import mark_safe
from ..models import MenuItem


register = template.Library()


def render_menu(menu_name, current_url, parent=None):
    menu_items = MenuItem.objects.filter(menu__name=menu_name, parent=parent).order_by('id')
    if not menu_items:
        return ''
    menu_html = '<ul>'
    for item in menu_items:
        active_class = 'active' if current_url == item.get_url() else ''
        menu_html += f'<li class="{active_class}"><a href="{item.get_url()}">{item.name}</a>'
        menu_html += render_menu(menu_name, current_url, parent=item)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info
    menu_html = render_menu(menu_name, current_url)
    return mark_safe(menu_html)
