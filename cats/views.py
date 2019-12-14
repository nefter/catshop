"""Cats app views"""

from django.shortcuts import render

from .models import Cat


def cats(request):
    cats = Cat.objects.all()
    return render(request, 'cats.html', {'cats': cats})
