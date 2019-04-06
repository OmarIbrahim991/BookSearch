from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("search"))
    return render(request, "main/index.html")

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("search"))
    return render(request, "main/signup.html")

def search(request):
    if request.user.is_authenticated:
        context = dict()
        context["title"] = request.user.username + "-Search"
        return render(request, "main/search.html", context)
    return HttpResponseRedirect(reverse("index"))

def profile(request):
    if not request.user.is_authenticated:
        return "<h1>Error1</h1>"
    context = dict()
    context["title"] = request.user.username
    return render(request, "main/profile.html", context)

def results(request):
    return

def book(request):
    return