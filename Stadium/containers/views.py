from django.shortcuts import render, redirect
import docker
from .models import container_details
# Create your views here.
PORT = 5000

def multiply(request):
  global PORT
  client = docker.from_env()
  print(client.images.list())
  while True:
    try:
      con = client.containers.run('stadium-api', ports={8000:PORT},detach = True)
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

  return redirect(f'http://127.0.0.1:'+str(PORT)+'/')



