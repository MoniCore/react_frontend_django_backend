from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
import math
import requests
import time
import datetime
import json
import os 

from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy



from blog.models import Posts,Likes,Comments,PostAttach,LikesComment,Replies,LikesReply
from account.models import CustomUser,Follows,Experience,Education,Visiter,Notification
from chat.models import Room,Message

from account.views import get_client_ip,get_geolocation_for_ip,get_random_string,get_curuser,get_users,get_users_following,get_following,get_followers,get_different_time,get_date_str,get_time_str

from groups.models import Group,GroupToUserInvite,FollowsGroup,LikeGroup,ViewsGroup
from pages.models import Page,PageToUserInvite,FollowsPage


import datetime
from datetime import timedelta
import random
import string
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from PIL import Image



def trollsdashboard(request):

    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user         
   
    users = []        
    users = get_users(request)   
    
    curuser = {}
    curuser = get_curuser(request,user.id)      
       
   
    
    return render(request,'trolls/dashboard.html',{'users':users,'curuser':curuser}) 