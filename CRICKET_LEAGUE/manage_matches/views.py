from django.shortcuts import render,reverse,redirect
from django.urls import reverse_lazy
from .models import Match,Point
# from .forms import MatchDetailForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.db.models import Sum
from manage_matches.models import Team


class MatchListView(ListView):
    model = Match
    template_name = 'manage_matches/match_list.html'

class MatchDetailView(DetailView):
    model = Match
    template_name = 'manage_matches/match_detail.html'

###########################################################
#####################points################################
###########################################################

class PointListView(ListView):
    model = Team
    def get_queryset(self):
        query_set = Team.objects.values('name').order_by('name').annotate(points=Sum('winner__winner_point'))
        return query_set
        
    template_name = 'manage_matches/point_list.html'


def home(request):
    return redirect('MatchList')