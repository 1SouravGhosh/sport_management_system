from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from .models import Group
from .forms import GroupDetailForm,FixtureDetailForm
from fixtures_points.models import Fixture
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
import random
from manage_matches.models import Point,Match
import manage_matches.urls
from django.contrib.auth.mixins import LoginRequiredMixin


class GroupCreateView(LoginRequiredMixin,CreateView):
    model = Group
    form_class = GroupDetailForm
    template_name = 'fixtures_points/group_create_update.html'

    def get_success_url(self):
        return reverse('GroupList')


class GroupUpdateView(LoginRequiredMixin,UpdateView):
    model = Group
    form_class = GroupDetailForm
    template_name = 'fixtures_points/group_create_update.html'
    
    def get_success_url(self):
        return reverse('GroupList')


class GroupListView(LoginRequiredMixin,ListView):
    model = Group
    template_name = 'fixtures_points/group_list.html'

# class GroupDetailView(DetailView):
#     model = Group
#     template_name = 'fixtures_points/group_detail.html'


class GroupDeleteView(LoginRequiredMixin,DeleteView):
    model = Group
    
    def get_success_url(self):
        return reverse_lazy('GroupList')

##############################################################################

##############################################################################

class FixtureCreateView(LoginRequiredMixin,CreateView):
    model = Fixture
    form_class = FixtureDetailForm
    template_name = 'fixtures_points/fixture_create_update.html'

    def get_success_url(self):
        return reverse('FixtureList')


class FixtureUpdateView(LoginRequiredMixin,UpdateView):
    model = Fixture
    form_class = FixtureDetailForm
    template_name = 'fixtures_points/fixture_create_update.html'
    
    def get_success_url(self):
        return reverse('FixtureList')


class FixtureListView(LoginRequiredMixin,ListView):
    model = Fixture
    template_name = 'fixtures_points/fixture_list.html'

class FixtureDetailView(LoginRequiredMixin,DetailView):
     model = Fixture
     template_name = 'fixtures_points/fixture_detail.html'


class FixtureDeleteView(LoginRequiredMixin,DeleteView):
    model = Fixture
    
    def get_success_url(self):
        return reverse_lazy('FixtureList')


######################################################################
######################################################################
class MatchSimulateView(LoginRequiredMixin,UpdateView):
    model = Fixture
    form_class = FixtureDetailForm
    template_name = 'fixtures_points/match_simulate.html'
    
    def choose_random_winner(self):
        self.match_id = 0
        query_set= Fixture.objects.filter(identifier=self.object.identifier)
        if query_set[0].completed:
            print("creating match")
            ls= [query_set[0].team1 ,query_set[0].team2]
            winner_team=random.choice(ls)
            point = Point.create(team=winner_team)
            match = Match.create(fixture=self.object,point=point)
            point.save()
            match.save()
            self.match_id = match.identifier
        else:
            print(query_set[0].identifier)
            match = Match.objects.filter(fixture__identifier=query_set[0].identifier)
            print(match)
            self.match_id = match[0].identifier
    
    def get_success_url(self):
        self.choose_random_winner()
        return reverse('MatchDetail',kwargs={'pk': self.match_id})

