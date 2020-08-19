from django.urls import path

from articles.views import one_article, view_all_articles

urlpatterns = [
    path('read/<str:name>', one_article, name='one_article'),
    path('', view_all_articles, name='view_all_articles'),
]
