from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from .models import Team
from .forms import TeamDetailForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamDetailForm
    template_name = 'manage_teams/team_create_update.html'

    def get_success_url(self):
        return reverse('TeamList')


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamDetailForm
    template_name = 'manage_teams/team_create_update.html'
    
    def get_success_url(self):
        return reverse('TeamDetail',kwargs={'pk': self.object.identifier})


class TeamListView(ListView):
    model = Team
    template_name = 'manage_teams/team_list.html'

class TeamDetailView(DetailView):
    model = Team
    template_name = 'manage_teams/team_detail.html'


class TeamDeleteView(DeleteView):
    model = Team
    def get_success_url(self):
        return reverse_lazy('TeamList')

