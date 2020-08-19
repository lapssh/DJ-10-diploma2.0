from django.db import models
from accounts.models import Customer
from shop.models import Product


class Order(models.Model):
    """
    Модель заказа используется менеджером, для отслеживания заказов покупателей.
    Описана ManyToMany связью покупателей с продуктами. Помнит дату заказа
    """
    customer = models.ForeignKey(Customer, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductsInOrder')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.created}'


class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар',
                                related_name='count_in_order', )
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество единиц товара')
