from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brewery(models.Model):
    brew_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    brewery_type = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    phone = models.IntegerField(blank=True, null=True)
    url = models.URLField(max_length=100, blank=True, null=True)
    saved_by_users = models.ManyToManyField(User, related_name='saved_breweries', blank=True)

    def __str__(self) -> str:
        return f"{self.name} in {self.city}"