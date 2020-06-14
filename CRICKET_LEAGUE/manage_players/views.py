from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from .models import Player
from .forms import PlayerDetailForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

class PlayerCreateView(LoginRequiredMixin,CreateView):
    model = Player
    form_class = PlayerDetailForm
    template_name = 'manage_players/player_create_update.html'

    def get_success_url(self):
        return reverse('PlayerList')


class PlayerUpdateView(LoginRequiredMixin,UpdateView):
    model = Player
    form_class = PlayerDetailForm
    template_name = 'manage_players/player_create_update.html'
    
    def get_success_url(self):
        return reverse('PlayerDetail',kwargs={'pk': self.object.identifier})


class PlayerListView(LoginRequiredMixin,ListView):
    model = Player
    template_name = 'manage_players/player_list.html'

class PlayerDetailView(LoginRequiredMixin,DetailView):
    model = Player
    template_name = 'manage_players/player_detail.html'


class PlayerDeleteView(LoginRequiredMixin,DeleteView):
    model = Player
    def get_success_url(self):
        return reverse_lazy('PlayerList')

