from django.db import models
from users.models import CustomerProfile
from transactions.models import Transaction

class GameImage(models.Model):
    image = models.ImageField()


class tags(models.Model):
    t_name = models.TextField()


class game(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tags = models.ManyToManyField(tags)
    images = models.ManyToManyField(GameImage)

    def __str__(self):
        return self.name


class game_owned(models.Model):
    customer = models.ForeignKey(CustomerProfile,on_delete=models.SET_NULL, null = True)
    game = models.ForeignKey(game, on_delete = models.SET_NULL, null = True)
    hours_played = models.IntegerField(default=0)
    rating = models.IntegerField(default = 0)
    transaction = models.OneToOneField(Transaction, on_delete=models.SET_NULL, null=True) 

    class Meta:
        unique_together = (("customer", "game"),)

    def __str__(self):
        return self.customer.Customer.username + '--' + self.game.name
