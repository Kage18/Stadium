from django.db import models
from users.models import CustomerProfile
# Create your models here.

class tags(models.Model):
    t_name = models.TextField()

class game(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits = 7, decimal_places=2)
    tags = models.ManyToManyField(tags)

class game_owned(models.Model):
    customer = models.ManyToManyField(CustomerProfile)
    game = models.ManyToManyField(game)
    hours_played = models.TimeField(auto_now_add=False)
    rating = models.IntegerField()
    

