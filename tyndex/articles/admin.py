from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')

admin.site.register(Article)