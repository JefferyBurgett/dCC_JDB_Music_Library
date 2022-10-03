from email.policy import default
from unittest.util import _MAX_LENGTH
from MySQLdb import Date
from django.db import models
from datetime import datetime, date
# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    # release_date = models.DateField(auto_now=False, auto_now_add=False, default= 'YYYY-MM-DD')
    genre = models.CharField(max_length=255)