from django.shortcuts import render
from .models import game_owned, game
# Create your views here.

def add_minute(request):
    game = request.POST['game_id']
    user = request.user
    g = game_owned.objects.filter(user=user, game=game.objects.get(pk=game))[0]
    g.hours_played += 1