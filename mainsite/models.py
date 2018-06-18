from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.username
    def __unicode__(self):
        return self.username
    class Meta:
        verbose_name='User'
        verbose_name_plural='User'
