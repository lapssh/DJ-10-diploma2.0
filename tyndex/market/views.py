from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from articles.models import Article


def index(request):
    try:
        articles = Article.objects.order_by('-published')
        context = {
            'articles': articles,
        }
        return render(request, 'articles.html', context)
    except SyntaxError as Errr:
        raise Http404('Ошбибка синтаксиса - ', Errr)
    except NameError as Errr:
        raise Http404('Name Error - ', Errr)
    except Exception as Errr:
        raise Http404("Возникла неучтенная ошибка, детали:  ", Errr)


def cart(request):
    template = loader.get_template('market/cart.html')
    context = {}
    return HttpResponse(template.render(context, request))


def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)
