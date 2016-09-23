from __future__ import unicode_literals
from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=30)
    Category_CHOICES = (
        ('portraits', 'Portrait'),
        ('landscapes', 'Landscape'),
	   ('streets', 'Street'),
	   ('designs', 'Design'),
	   ('still-life', 'Still life'),
    )
    category = models.CharField(max_length=10, choices=Category_CHOICES)
    image = models.ImageField (upload_to="images/",null=True,blank=True,
            width_field='width_field',
            height_field='height_field',)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    Size_CHOICES = (
        ('portraits', 'Portrait'),
        ('landscapes', 'Landscape'),
    )
    size = models.CharField(max_length=10, choices=Size_CHOICES)


    def __str__(self):
        return self.name
