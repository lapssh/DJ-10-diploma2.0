from django.http import Http404
from django.shortcuts import render

from articles.models import Article


def view_all_articles(request):
    articles = Article.objects.order_by('-created')

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)


def one_article(request, name=None):
    articles = Article.objects.filter(name=name)
    context = {'articles': articles}
    article = Article.objects.filter(name=name).first()
    if not article:
        raise Http404('Error 404! Sorry')
    return render(request, 'articles.html', context)
