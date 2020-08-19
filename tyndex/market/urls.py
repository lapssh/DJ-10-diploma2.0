from django.urls import path, include

from orders.views import order_view
from .views import cart
from .views import index

handler404 = 'market.views.handler404'

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cart.html', cart, name='cart'),
    path('order/', order_view, name='order'),
]
