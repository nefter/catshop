"""Cats admin site"""

from django.contrib import admin

from .models import Cat


admin.site.register(Cat)
