from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register([game, game_owned, tags, GameImage])

