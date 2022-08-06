from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from .forms import customUserCreactionForm
from .models import CustomUser,Audio_Store
import eyed3


# Create your views here.

def home(request):
    return render(request,"home.html")

def SignUp(request):
    form = customUserCreactionForm
    if request.method == "POST":
        form = customUserCreactionForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_user = True
            f.save()
            return redirect(Login)
    return render(request, "signup.html", {"form": form})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password = password)
        if user and user.is_user == True:
            login(request, user)
            return redirect(audiostore)
        else:
            return HttpResponse('Invalid login details')
    return render(request,"login.html")

def audiostore(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            adfiles = Audio_Store.objects.filter(user=user)
            audio = request.FILES.get("audio")
            if audio:
                data = Audio_Store(user=request.user,record=audio)
                audio = ""
                data.save()
                return render(request,"audioupload.html",{"adfiles":adfiles})
            return render(request, "audioupload.html", {"adfiles": adfiles})
        user = request.user
        adfiles = Audio_Store.objects.filter(user=user)
        return render(request, "audioupload.html", {"adfiles": adfiles})
    return redirect(Login)

def Delete(request):
    if request.method == "POST":
        record = request.POST.get("record")
        user = request.user
        data = Audio_Store.objects.get(user=user,record=record)
        data.delete()
    else:
        return redirect(audiostore)
    return redirect(audiostore)



def Logout(request):
    logout(request)
    return home(request)





