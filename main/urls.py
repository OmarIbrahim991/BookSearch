from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("signup/", views.signup, name="signup"),
        path("search/", views.search, name="search"),
        path("profile/", views.profile, name="profile"),
        path("results/", views.results, name="results"),
        path("book/<str:isbn>", views.book, name="book"),
]