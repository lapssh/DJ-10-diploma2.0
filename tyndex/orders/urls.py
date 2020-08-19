from django.urls import path

from orders.views import show_cart_view, add_to_cart

urlpatterns = [
    path('cart/', show_cart_view, name='show_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]
