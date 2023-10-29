from django.db import models
from django.utils.text import slugify


class TitleSlugAbstract(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title


class Menu(TitleSlugAbstract):
    
    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'
        ordering = ['title']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Menu, self).save(*args, **kwargs)

    
class Category(TitleSlugAbstract):
    category_url = models.CharField(max_length=2000,
                                    null=True,
                                    blank=True)
    menu = models.ForeignKey(Menu, 
                             on_delete=models.PROTECT,
                             related_name='categories')
    parent_category = models.ForeignKey('self',
                                      on_delete=models.PROTECT,
                                      related_name='sub_categories',
                                      blank=True,
                                      null=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.category_url:
            if not self.parent_category:
                self.category_url = self.slug
            else:
                self.category_url = self.parent_category.category_url + '/' + self.slug 
        super(Category, self).save(*args, **kwargs)
