from django.contrib import admin

from menu.models import Category, Menu


class SubCategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    verbose_name = 'Subcategory'
    verbose_name_plural = 'Subcategories'


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [SubCategoryInline]
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [CategoryInline]
    prepopulated_fields = {'slug': ('title', )}
