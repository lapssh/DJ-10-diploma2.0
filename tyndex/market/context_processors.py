from market.models import Section


def menu_items(request):
    context = {'menu': Section.objects.prefetch_related('categories').all()}

    return context
