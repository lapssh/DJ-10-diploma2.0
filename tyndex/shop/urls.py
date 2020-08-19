from django.urls import path

from shop.views import product_list_view, product_view

urlpatterns = [
    path('product_list_view', product_list_view, name='product_list_view'),
    path('<str:section_slug>/<str:category_slug>/<str:slug>', product_view, name='product'),
    path('<str:section_slug>/<str:category_slug>', product_list_view, name='products'),
    path('', product_list_view, name='products'),
]
