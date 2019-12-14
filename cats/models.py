"""Cats app model"""

from django.db import models


class Cat(models.Model):
    """Cat model"""
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    breed = models.CharField(max_length=20)

    def __str__(self):
        """String representation of a cat"""
        return self.name
