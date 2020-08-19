from django.http import Http404
from django.shortcuts import render

from articles.models import Article


def view_all_articles(request):
    try:
        articles = Article.objects.order_by('-created')

        context = {
            'articles': articles,
        }
        return render(request, 'index.html', context)
    except SyntaxError as Errr:
        raise Http404('Ошбибка синтаксиса - ', Errr)
    except NameError as Errr:
        raise Http404('Name Error - ', Errr)
    except Exception as Errr:
        raise Http404("Возникла неучтенная ошибка, детали:  ", Errr)


def one_article(request, name=None):
    try:
        articles = Article.objects.filter(name=name)
        context = {'articles': articles}
        article = Article.objects.filter(name=name).first()
        if not article:
            raise Http404('Error 404! Sorry')
        return render(request, 'articles.html', context)
    except SyntaxError as Errr:
        raise Http404('Ошбибка синтаксиса - ', Errr)
    except NameError as Errr:
        raise Http404('Name Error - ', Errr)
    except Exception as Errr:
        raise Http404("Возникла неучтенная ошибка, детали:  ", Errr)
