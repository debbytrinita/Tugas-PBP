from django.urls import path
from todolist.views import *


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/',register, name='register'),
    path('create-task/',add_new_task, name='add_new_task'),
    path('logout/',logout_user,name='logout'),
    path('json/',get_todolist_json,name='get_todolist_json'),
    path('add/',add,name='add'),
]