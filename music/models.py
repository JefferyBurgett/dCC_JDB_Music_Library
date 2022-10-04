
from MySQLdb import Date
from django.db import models
from datetime import datetime, date
# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField('YYYY-MM-DD')
    genre = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)