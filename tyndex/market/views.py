
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from articles.models import Article




def index(request):
    try:
        print('=' * 80)
        articles = Article.objects.order_by('-published')

        context = {
            'articles': articles,

        }
        print('контекст статей')
        print(context)

        return render(request, 'articles.html', context)
    except Exception as Errr:
        raise Http404("Page does not exist - ", Errr)





def cart(request):
    template = loader.get_template('market/cart.html')
    context = {}
    return HttpResponse(template.render(context, request))





def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)






