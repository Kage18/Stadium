from django.db import models

# Create your models here.


class container_details(models.Model):
  port = models.IntegerField(unique = True)
  container_id = models.CharField(max_length=15, blank=True, null=True)