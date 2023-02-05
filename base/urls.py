from django.urls import path
from . import views

urlpatterns = [
    # Login route
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),

    # CRUD routes
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>', views.update_room, name='update-room'),
    path('delete-room/<str:pk>', views.delete_room, name='delete-room'),
]
