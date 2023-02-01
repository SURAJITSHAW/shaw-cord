from django.contrib import admin

# Register your models here.

from base.models import Room, Message, Topic

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
