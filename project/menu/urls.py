from django.urls import path

from menu import views


app_name = 'menu'


urlpatterns = [
    path('<slug:menu_slug>/<path:categories_slugs>/', views.menu, name='menu_with_categories'),
    path('<slug:menu_slug>/', views.menu, name='menu'),
    path('', views.menu, name='home'),
]