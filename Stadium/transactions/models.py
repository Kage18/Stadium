from django.db import models
from users.models import CustomerProfile
# Create your models here.


class Transaction(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
