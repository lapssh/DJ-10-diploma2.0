from django.contrib import admin

from market.models import Section
from .models import Category

admin.site.register(Section)
admin.site.register(Category)

