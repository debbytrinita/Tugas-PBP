from todolist.forms import todolist_form
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
    'data_todolist' : data_todolist,
    'username': request.COOKIES['username'],
    'last_login' : request.COOKIES['last_login'],
}
    return (render(request, "todolist.html",context))

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            response.set_cookie('username', username)
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def add_new_task(request):
    if request.method == "POST":
        form = todolist_form(request.POST)
        if form.is_valid():
            username = request.user
            date_user = datetime.date.today()
            title_user = request.POST.get('title')
            description_user = request.POST.get('description')
            new_task = Task(user=username,date=date_user.strftime("%Y-%m-%d"),title=title_user,description=description_user)
            new_task.save()
           
            return HttpResponseRedirect(reverse('todolist:show_todolist'))

    context ={'form': todolist_form

    }

    return render(request, 'add_new_task.html', context)
