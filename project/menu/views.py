from django.shortcuts import render


def menu(request, menu_slug=None, categories_slugs=None):
    if not menu_slug:
        return render(request, 'index.html')
    return render(request, 'index.html', {
        'menu_slug': menu_slug,
        'categories_slugs': categories_slugs,
    })
