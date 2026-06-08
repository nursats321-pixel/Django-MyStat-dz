from django.shortcuts import (
    render, redirect
)  
from django.contrib.auth.models import User

from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        
        username = request.POST.get('username') 
        
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            
            return render(request, "user_have.html")

        
        
        User.objects.create_user(
            username= username,
            password= password
        )
        
        return render(request, "login.html")
    
    return render(request, "register.html")
        

def login_view(request):

        
        if request.method == 'POST':
            return redirect('/admin/')


        return render(request, "login.html")

