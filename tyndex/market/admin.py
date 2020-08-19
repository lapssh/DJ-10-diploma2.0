from django.contrib import admin

from accounts.models import Customer
from articles.models import Article
from market.models import Section
from orders.models import Order
from orders.models import ProductsInOrder
from shop.models import Product
from .models import Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder

    verbose_name = 'Заказанный товар'
    verbose_name_plural = 'Заказанные товары'


class OrderAdmin(admin.ModelAdmin):
    ordering = ('created', 'id')
    list_display = ('customer', 'quantity', 'created',)
    inlines = (ProductsInOrderInline,)

    def quantity(self, obj):
        return ProductsInOrder.objects.filter(order=obj).count()

    quantity.short_description = 'Количество единиц'


admin.site.register(Article)
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
