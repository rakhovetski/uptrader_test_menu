from django import template

from menu.models import  Menu


register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_another_menu(menu_slug, categories_slugs=None):
    categories_slugs_list = None
    actual_category = None

    if categories_slugs:
        categories_slugs_list = categories_slugs.split('/')
        actual_category = categories_slugs_list.pop(0)
    
    try:
        menu = Menu.objects.prefetch_related('categories').get(slug=menu_slug)
    except Menu.DoesNotExist:
        return {}
    
    categories = menu.categories.filter(parent_category=None)

    return {'menu': menu,
            'categories': categories,
            'categories_slugs_list': categories_slugs_list,
            'actual_category': actual_category}



@register.inclusion_tag('menu/child.html')
def draw_child_categories(category, categories_slugs_list):
    actual_slug = None
    last_slug = None
    
    if categories_slugs_list and len(categories_slugs_list) > 0:
        last_slug = categories_slugs_list[-1]
        actual_slug = categories_slugs_list.pop(0)

    return {
        'menu': category.menu,
        'category': category,
        'actual_slug': actual_slug,
        'last_slug': last_slug,
        'categories_slugs_list': categories_slugs_list
    }