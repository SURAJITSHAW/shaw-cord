from django.shortcuts import render
from base.models import Room

# test data 
# rooms = [
#     {'id': 1, 'name': 'Learn Django together'},
#     {'id': 2, 'name': 'Backend developers only!'},
#     {'id': 3, 'name': 'OP verse'},
# ]

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'room.html', context)