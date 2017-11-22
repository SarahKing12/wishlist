# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render
from .models import User 
from django.contrib import messages

#route: '/main'
def index(request):
    #User.objects.all().delete()  #Clears database by refreshing browser! This is awesome! 
    return render(request, 'python_exam_login_app/index.html')

######This is where the data for the registration form is going through to post in the database
#route: '/register'
def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
####CHANGE THIS IF I WANT TO REDIRECT TO ANOTHER PAGE ONCE REGISTERED############        
        messages.success(request, "Added successfully!")
    else:
        for error in results['errors']:
            messages.error(request, error)

    return redirect('/dashboard')

#route: '/login'
def login(request): 
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, "Please check your username and password and try again.")
        return redirect('/main')
    request.session['user_name'] = results['user'].user_name 
    request.session['name'] = results['user'].name
    request.session['user'] = results['user'].id
    return redirect('/dashboard')

#route: '/dashboard'
#def dashboard(request):
    #if 'user_name' not in request.session:
        #return redirect ('/')
    #return render(request, 'python_exam_login_app/dashboard.html')

#route: '/logout'
def logout(request):
    request.session.flush()
    return redirect ('/main')