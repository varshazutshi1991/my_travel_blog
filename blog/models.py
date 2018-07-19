from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    travel_place = models.CharField(max_length=100)
    travel_date = models.DateField(default=datetime.today)
    travel_story = models.TextField()
    travel_images = models.ImageField(upload_to='media/')
    slug = models.SlugField(max_length=100, db_index=True)
    blogger = models.ForeignKey('Blogger', on_delete=models.CASCADE)

    # def travel_date(self):
    #     self.travel_date = datetime.datetime.now()
    #     self.save()

    def __unicode__(self):
        return '%s' % self.title


class Blogger(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return '%s' % self.name