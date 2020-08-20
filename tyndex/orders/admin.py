from django.contrib import admin

from orders.models import ProductsInOrder, Order


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


admin.site.register(Order, OrderAdmin)
