from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(game)
admin.site.register(game_owned)
admin.site.register(tags)