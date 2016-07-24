from django.db import models

# Create your models here.
class User(models.Model):
    usename = models.CharField(max_length=30)
    headImage = models.FileField(upload_to='upload/')

    def __unicode__(self):
        return self.usename
