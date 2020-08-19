from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from market.views import index

urlpatterns = [
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('articles/', include('articles.urls')),
                  path('market/', include('market.urls')),
                  path('shop/', include('shop.urls')),
                  path('order/', include('orders.urls')),
                  path('index.html', index, name='index'),
                  path('', index),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
