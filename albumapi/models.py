from django.db import models

# Create your models here.

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    image =  models.URLField(max_length=255)
    thumbnail = models.URLField(max_length=255)

    def __str__(self):
        return self.title
