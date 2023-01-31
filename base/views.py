from django.shortcuts import render

# test data 
rooms = [
    {'id': 1, 'name': 'Learn Django together'},
    {'id': 2, 'name': 'Backend developers only!'},
    {'id': 3, 'name': 'OP verse'},
]

# Create your views here.

def home(request):
    # context = {'rooms': rooms}
    return render(request, 'home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'room.html', context)