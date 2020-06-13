from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from .models import Match
# from .forms import MatchDetailForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# class MatchCreateView(CreateView):
#     model = Match
#     form_class = MatchDetailForm
#     template_name = 'manage_matches/match_create_update.html'

#     def get_success_url(self):
#         return reverse('MatchList')

class MatchListView(ListView):
    model = Match
    template_name = 'manage_matches/match_list.html'

class MatchDetailView(DetailView):
    model = Match
    template_name = 'manage_matches/match_detail.html'

