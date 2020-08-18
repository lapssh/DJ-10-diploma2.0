from django.urls import path

from market.views import view_all_articles, one_article

urlpatterns = [
    path('read/<str:name>', one_article, name='one_article'),
    path('', view_all_articles, name='view_all_articles'),
]
