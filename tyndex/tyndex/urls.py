from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from market.views import index, view_all_articles, one_article, product_view, product_list_view, show_cart_view, \
    add_to_cart

urlpatterns = [
                  path('index.html', index, name='index'),
                  path('', index),
                  path('market/', include('market.urls')),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('articles/read/<str:name>', one_article, name='one_article'),
                  path('articles/', view_all_articles, name='view_all_articles'),
                  path('product_list_view', product_list_view, name='product_list_view'),
                  path('<str:section_slug>/<str:category_slug>/<str:slug>', product_view, name='product'),
                  path('<str:section_slug>/<str:category_slug>', product_list_view, name='products'),
                  path('', product_list_view, name='products'),
                  path('cart/', show_cart_view, name='show_cart'),
                  path('add_to_cart/', add_to_cart, name='add_to_cart'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
