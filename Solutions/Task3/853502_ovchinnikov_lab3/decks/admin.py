from django.contrib import admin

from .models import Arthetype, Deck, Deck_Picture, Deck_Review, Player

admin.site.register(Arthetype)
admin.site.register(Deck)
admin.site.register(Deck_Picture)
admin.site.register(Deck_Review)
admin.site.register(Player)
