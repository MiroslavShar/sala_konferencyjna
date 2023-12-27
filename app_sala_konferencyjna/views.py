from curses.ascii import isdigit

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
        capacity_hall = request.POST['capacity_hall']
        availability_of_projector = request.POST.get('availability_of_projector')
        capacity_hall = int(capacity_hall)
        if availability_of_projector == 'on':
            availability_of_projector = True
        else:
            availability_of_projector = False
        h = Hall(name_hall=name_hall, capacity_hall=capacity_hall, availability_of_projector=availability_of_projector)
        h.save()
        return render(request, 'base.html')

def show_all_halls(request):
    halls = Hall.objects.all()
    name_hall_show = request.GET.get('name_hall', '')
    capacuty_hall_show = request.GET.get('capacity_hall', '')
    if name_hall_show != '':
        halls = halls.filter(name_hall__icontains=name_hall_show)
    if capacuty_hall_show != '':
        halls = halls.filter(capacity_hall__exact=capacuty_hall_show)
    return render(request, 'all_halls.html', context={'halls': halls})

def hall_detail(request, id):
    show_hall_detail = Hall.objects.get(id=id)
    return render(request, 'detail_hall.html', context={'halls_detail': show_hall_detail})


# Create your views here.
