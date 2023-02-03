import re
from django.shortcuts import render, redirect
from django.db.models import Q
from base.models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# test data
# rooms = [
#     {'id': 1, 'name': 'Learn Django together'},
#     {'id': 2, 'name': 'Backend developers only!'},
#     {'id': 3, 'name': 'OP verse'},
# ]

# Create your views here.

def loginPage(request):

    # if user is logged in, redirect to the home page
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
        except: 
            messages.error(request, "User doesn't esists.")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User or Password does not exist!')

    context = {}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    return render(request, 'home.html', {'rooms': rooms, 'topics': topics, 'room_count': room_count})


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'room.html', context)


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()

    # Process the data get from the Post request
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'create_room.html', context)


@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)  # the room we want to update
    form = RoomForm(instance=room)

    # Resttricted permissions
    if request.user != room.host:
        return HttpResponse("You are not allowed to update this room!")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'create_room.html', context)


@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)  # the room we want to delete

    # Resttricted permissions
    if request.user != room.host:
        return HttpResponse("You are not allowed to delete this room!")

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'delete.html', {'obj': room})
