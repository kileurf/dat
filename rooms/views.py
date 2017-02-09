from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Room
from .forms import RoomForm

def index(request):
    latest_rooms_list = Room.objects.all()
    context = {'latest_rooms_list': latest_rooms_list}
    return render(request, 'rooms/index.html', context)

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rooms:index'))
    else:
        form = RoomForm()

    return render(request, 'rooms/room.html', {'form': form})

@login_required
def modify_room(request, slug):
    room = get_object_or_404(Room, slug=slug)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rooms:index'))
    else:
        form = RoomForm(instance=room)

    return render(request, 'rooms/room.html', {'form': form})

@login_required
def delete_room(request, slug):
    room = get_object_or_404(Room, slug=slug).delete()

    return HttpResponseRedirect(reverse('rooms:index'))
