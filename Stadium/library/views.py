from django.shortcuts import render
from django.http import HttpResponse
from .models import game_owned, game
from users.models import CustomerProfile
# Create your views here.

def add_minute(request):
    game_id = int(request.POST['game_id'])
    userId = int(request.POST['user_id'])
    time = int(request.POST['time'])
    time = int(time)//60
    user = CustomerProfile.objects.get(pk=userId)
    g = game_owned.objects.filter(customer=user, game=game.objects.get(pk=game_id))[0]
    g.hours_played += time
    g.save()
    return HttpResponse("OK", status=200)