from django.shortcuts import render, redirect
from django.db.models import Q
from base.models import Room, Topic
from .forms import RoomForm

# test data
# rooms = [
#     {'id': 1, 'name': 'Learn Django together'},
#     {'id': 2, 'name': 'Backend developers only!'},
#     {'id': 3, 'name': 'OP verse'},
# ]

# Create your views here.


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


def update_room(request, pk):
    room = Room.objects.get(id=pk)  # the room we want to update
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'create_room.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)  # the room we want to delete

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'delete.html', {'obj': room})
