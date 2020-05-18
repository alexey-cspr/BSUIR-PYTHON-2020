from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from decks.models import Deck


class DeckView(View):
    def get(self, request):
        decks = Deck.objects.all()
        return render(request, "decks/main_page.html", {"deck_list": decks})

class DecksView(View):
    def get(self, request, slug):
        decks = Deck.objects.filter(name=slug)
        return render(request, "decks/decks_list.html", {"decks": decks})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
