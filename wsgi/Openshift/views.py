import os
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.http import HttpRequest
from models import silverusers
from datetime import datetime

def home(request):
    silveruserA = silverusers()
    silveruserA.user_name = "zhiwei"
    silveruserA.user_description = "test write database!"
    silveruserA.user_bd = datetime(1983,8,15)
    silveruserA.save()
    
    html = "<H1>"
    if request.user.is_authenticated():
        html += "User is authenticated. "
    else:
        html += "User is not authenticated,"
     
    if request.method == "GET":
        html += "Get method used"
    elif request.method == "POST":
        html += "Post method used"
    else:
        html += "Other method, " + request.method + ", used. "     
    
    html += "</H1><HR>"
        
    return HttpResponse(html)
#    return render_to_response('home/test.htm')