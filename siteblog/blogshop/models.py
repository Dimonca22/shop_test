from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Url', unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT, related_name='products')
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, verbose_name='Url', db_index=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    views = models.IntegerField(default=0,verbose_name='Кол-во просмотров')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title
