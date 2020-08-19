from django.db import models

from shop.models import Product


class Article(models.Model):
    """
    Модель описывает новости на сайте
    Модель имеет заголовок, текст статьи и дату публикации.
    Есть привязка к товарам, продаваемым в магазине.
    """
    title = models.CharField(max_length=200, verbose_name='Кликбейтный заголовок')
    text = models.TextField(max_length=1500, verbose_name='Содержание статьи')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    products = models.ManyToManyField(Product, verbose_name='Связанные товары', blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title