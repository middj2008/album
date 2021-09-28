from django.db import models
import PIL

# Create your models here.

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='image')
    thumbnail = models.ImageField(upload_to='image')

    def __str__(self) -> str:
        return self.title
