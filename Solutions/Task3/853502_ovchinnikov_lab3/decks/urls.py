from django.urls import path

from . import views

urlpatterns = [
    path("", views.DeckView.as_view(), name="home"),
    path("decks_list/<slug:slug>", views.DecksView.as_view()),
    path("accounts/signup/", views.signup, name="signup")
]