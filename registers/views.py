from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.urls import reverse

# Create your views here.
def signin(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
    except:
        return render(request, "main/index.html", {"message": "Please enter your username and password first."})
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "main/index.html", {"message": "Wrong username or password."})
        

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "main/signup.html", {"form": form})