from django.db import models
from django.contrib.auth.models import User
from users.models import CustomerProfile
from library.models import game
from transactions.models import Transaction
# Create your models here.


class MerchImage(models.Model):
    image = models.ImageField()


class Merchandise(models.Model):
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    shown = models.BooleanField(default=True)
    images = models.ManyToManyField(MerchImage)


class MerchUser(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    merch = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
