from django import template
from app.models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu_list.html', takes_context=True)
def draw_menu(context, name):
    menu_list = Menu.objects.filter(category__name=name).select_related("parent")
    active_item = context['request'].path.replace("/", "")
    data = {
        "menu_list": menu_list,
        "active_item": active_item,
    }
    return data


@register.inclusion_tag('menu/children_menu.html', takes_context=True)
def get_menu_children(context, parent_id, is_children=False):
    query = context["menu_list"]
    children_list = []
    for children in query:
        if children.parent_id == parent_id:
            children_list.append(children)

    context["children_menu"] = children_list
    context["class"] = "submenu dropdown-menu" if is_children else "dropdown-menu"
    return context
