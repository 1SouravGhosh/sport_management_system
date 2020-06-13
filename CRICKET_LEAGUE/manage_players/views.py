from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from .models import Player
from .forms import PlayerDetailForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerDetailForm
    template_name = 'manage_players/player_create_update.html'

    def get_success_url(self):
        return reverse('PlayerList')


class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerDetailForm
    template_name = 'manage_players/player_create_update.html'
    
    def get_success_url(self):
        return reverse('PlayerDetail',kwargs={'pk': self.object.identifier})


class PlayerListView(ListView):
    model = Player
    template_name = 'manage_players/player_list.html'

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'manage_players/player_detail.html'


class PlayerDeleteView(DeleteView):
    model = Player
    def get_success_url(self):
        return reverse_lazy('PlayerList')

