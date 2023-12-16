from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from app_sala_konferencyjna.models import Hall

def add_new_hall(request):
    if request.method == 'GET':
        response = render(request, 'add_room.html')
        return response
    else:
        name_hall = request.POST['name_hall']
        capacuty_hall = request.POST['capacity_hall']
        h = Hall(name_hall=name_hall, capacity_hall=capacuty_hall)
        h.save()
        return render(request,'new_room.html', context={'hall':h})


# Create your views here.
