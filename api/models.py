from django.db import models
from django.urls import reverse

# Create your models here.

class City(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Event(models.Model):

    name = models.CharField(max_length=100)
    date_of_event = models.DateTimeField(null=True, blank=True)
    city = models.ManyToManyField(City, blank=True, default=None)#One event can be in a few cities
    price = models.IntegerField(null=True, blank=True)
    tickets_left = models.IntegerField(null=True, blank=True)

    #When we save model, we check the day of the week, and set fitting price
    def save(self, *args, **kwargs):
        day_of_week = self.date_of_event.weekday()
        if (day_of_week >= 0 and day_of_week < 5):
            self.price = default = 3000
        else:
            self.price = default = 6000
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name