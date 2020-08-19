from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from market.views import index
from orders.views import show_cart_view, add_to_cart
from shop.views import product_view, product_list_view

urlpatterns = [
                  path('accounts/', include('accounts.urls')),
                  path('articles/', include('articles.urls')),

                  path('index.html', index, name='index'),
                  path('shop/', include('shop.urls')),
                  path('market/', include('market.urls')),

                  path('', index),

                  path('admin/', admin.site.urls),
                  path('product_list_view', product_list_view, name='product_list_view'),
                  path('<str:section_slug>/<str:category_slug>/<str:slug>', product_view, name='product'),
                  path('<str:section_slug>/<str:category_slug>', product_list_view, name='products'),
                  path('', product_list_view, name='products'),
                  path('cart/', show_cart_view, name='show_cart'),
                  path('add_to_cart/', add_to_cart, name='add_to_cart'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
