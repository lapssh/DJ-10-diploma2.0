from django.db import models

from market.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    price = models.DecimalField(max_digits=12, blank=False, verbose_name='Цена', decimal_places=2, default=0)
    product_number = models.IntegerField(blank=False, verbose_name='Артикул товара', unique=True)
    img = models.ImageField(upload_to='media/img/', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=512, verbose_name='Описание')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


