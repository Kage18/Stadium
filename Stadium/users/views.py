from django.shortcuts import render
import jwt
from django.shortcuts import redirect, render
 
from users.models import User
from Stadium.settings import SECRET_KEY, DOMAIN
 
 
def activate_account(request, token):
    username = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])["user"]
    user = User.objects.get(username=username)
    if username and not user.is_verified:
        user.is_verified = True
        user.save()
    return redirect(f'http://127.0.0.1:3000/login/')
      
# Create your views here.
