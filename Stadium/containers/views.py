from django.shortcuts import render, redirect
import docker
from .models import container_details
from library.models import *
from django.http import JsonResponse
import time 
# Create your views here.
PORT = 5000

def multiply(request,pk,userid):
  global PORT
  client = docker.from_env()
  Game = game.objects.get(pk=pk)
  url = 'http://10.0.55.121:8000'
  print(url)
  print(client.images.list())
  while True:
    try:
      # con = client.containers.run('game-server', ports={8000:PORT},detach = True, environment=['ROM_URL='+url])
      con = client.containers.run('game-server', ports={8000:PORT},detach = True, environment=['ROM_URL='+url+Game.rom.url, 'ENDPOINT='+url+'/add_time/', 'GAME_ID='+str(pk),'USER_ID='+str(userid)])
      # con = client.containers.run('game-server', ports={8000:PORT},detach = True, environment=['ROM_URL='+url])
      break
    except:
      PORT += 1
      if PORT%8888 == 0:
        PORT = 5000
    else:
      PORT += 1
      if PORT%8888 == 0:
        PORT = 5000
      break

  print(client.containers.list())
  data = {
      'url' : 'ws://10.0.55.121:'+str(PORT)+'/'
    }
  time.sleep(10)
  # return redirect(f'http://127.0.0.1:'+str(PORT)+'/')
  return JsonResponse(data)


