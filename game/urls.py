from django.urls import path
from game.views import *

urlpatterns = [
    path('play',play, name="play"),
    path('fetch',fetch, name="fetch"),
    path('playerlist',playerList.as_view(), name="playerlist"),
    path('gamemasterlist/<int:id>',gamemasterList.as_view(), name="gamemasterlist1"),
    path('gamemasterlist',gamemasterList.as_view(), name="gamemasterlist"),
]