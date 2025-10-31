from django.db import models
import datetime

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.title} - {self.id}"


class Area(models.Model):
    main_area = models.CharField(max_length=100)
    story_area = models.TextField()
    popular_place = models.TextField()

class City(models.Model):
    title = models.CharField(max_length=100)
    story_city = models.TextField()









