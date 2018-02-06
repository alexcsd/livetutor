from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request, 'blogask/index.html')
def register_user(request):
    form = UserCreationForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'blogask/register.html',{'form':form,'error_message':'wrong auth'})

    return render(request, 'blogask/register.html',{'form':form})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'blogask/login.html', {'error_message':'wrong auth'})

    return render(request, 'blogask/login.html')
def logout_user(request):
    logout(request)
    return redirect('index')