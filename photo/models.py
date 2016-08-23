from __future__ import unicode_literals
from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=30)
    Category_CHOICES = (
        ('portraits', 'Portrait'),
        ('landscapes', 'Landscape'),
	('streets', 'Street'),
	('designs', 'Design'),
    )
    category = models.CharField(max_length=10, choices=Category_CHOICES)
    image = models.ImageField (upload_to="images/",null=True,blank=True)


    def __str__(self):
        return self.name
