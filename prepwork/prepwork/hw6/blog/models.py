from django.db import models

# Create your models here.

class Auther(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    authers = models.ManyToManyField(Auther)
    
    def __unicode__(self):
        return self.name

