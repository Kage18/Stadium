from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from django.db.models.signals import post_save

# Create your models here.
class CustomerProfile(models.Model):
    Customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cus')
    DOB = models.DateField()
    gender = models.IntegerField()
    phone_no = models.IntegerField()
    bio = models.TextField(null = True)
    joined  = models.DateField(auto_now_add = True)
    avatar = models.TextField(null = True)
    

    def __str__(self):
        return self.Customer.username

# def post_save_customerprofile_create(sender, instance, created, *args, **kwargs):
#     if created:
#         CustomerProfile.objects.get_or_create(Customer=instance)



# post_save.connect(post_save_customerprofile_create, sender=User)


class VendorProfile(models.Model):
    Vendor = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ven')
    api_key = models.TextField(null = True)
    active = models.BooleanField()
    joined  = models.DateField(auto_now_add = True)

    

    def __str__(self):
        return self.Vendor.username