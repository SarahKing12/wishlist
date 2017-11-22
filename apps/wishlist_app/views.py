# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render 
from ..python_exam_login_app.models import User 
from .models import Item
#from django.core.urlresolvers import reverse
#from models import *

#route: '/dashboard'
def dashboard(request):
    if 'user_name' not in request.session:
        return redirect ('/main')
    return render(request, 'wishlist_app/index.html')

def create(request):
    return render(request, 'wishlist_app/create.html')

def add(request):
    ###################################I was able to get the items added to the database without the liked_item = people, but they weren't relating to the user
    #people = User.objects.get(id=request.session['user'])
    Item.objects.create(
        item_name = request.POST['item_name'],
        #liked_item = people

        )
    return redirect ('/wish_list/create')

#route: '/logout'
def logout(request):
    request.session.flush()
    return redirect ('/main')
