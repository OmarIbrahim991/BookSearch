from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Book
from os import environ
from requests import get

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
        return render(request, "main/search.html")
    return HttpResponseRedirect(reverse("index"))

def profile(request):
    if not request.user.is_authenticated:
        return "<h1>Error1</h1>"
    context = dict()
    context["title"] = request.user.username
    return render(request, "main/profile.html", context)

def results(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    context = dict()
    try:
        context["text"] = request.POST["search"]
    except:
        return HttpResponseRedirect(reverse("index"))
    context["result"] = Book.objects.filter(isbn__icontains = context["text"]) \
    | Book.objects.filter(title__icontains = context["text"]) \
    | Book.objects.filter(author__icontains = context["text"])
    try:
        year = int(context["text"])
        context["result"] = context["result"] | Book.objects.filter(year=year)
    except:
        context["result"] = context["result"].order_by("-year")
        return render(request, "main/results.html", context)
    context["result"] = context["result"].order_by("-year")
    return render(request, "main/results.html", context)

def book(request, isbn):
    context = dict()
    context["isbn"] = isbn
    good_reads = environ.get("GOOD_READS")
    if type(good_reads) == str:
        good_reads = good_reads.strip('\"')
    resp = get("https://www.goodreads.com/book/review_counts.json", params={"key": good_reads, "isbns": isbn})
    if resp.ok:
        context["details"] = resp.json()['books'][0]
        return render(request, "main/book.html", context)
    raise Http404("No book matches with the provided ISBN.")