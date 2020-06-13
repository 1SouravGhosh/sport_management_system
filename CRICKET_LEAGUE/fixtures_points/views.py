from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from .models import Group
from .forms import GroupDetailForm,FixtureDetailForm
from fixtures_points.models import Fixture
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupDetailForm
    template_name = 'fixtures_points/group_create_update.html'

    def get_success_url(self):
        return reverse('GroupList')


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupDetailForm
    template_name = 'fixtures_points/group_create_update.html'
    
    def get_success_url(self):
        return reverse('GroupList')


class GroupListView(ListView):
    model = Group
    template_name = 'fixtures_points/group_list.html'

# class GroupDetailView(DetailView):
#     model = Group
#     template_name = 'fixtures_points/group_detail.html'


class GroupDeleteView(DeleteView):
    model = Group
    
    def get_success_url(self):
        return reverse_lazy('GroupList')

##############################################################################

##############################################################################

class FixtureCreateView(CreateView):
    model = Fixture
    form_class = FixtureDetailForm
    template_name = 'fixtures_points/fixture_create_update.html'

    def get_success_url(self):
        return reverse('FixtureList')


class FixtureUpdateView(UpdateView):
    model = Fixture
    form_class = FixtureDetailForm
    template_name = 'fixtures_points/fixture_create_update.html'
    
    def get_success_url(self):
        return reverse('FixtureList')


class FixtureListView(ListView):
    model = Fixture
    template_name = 'fixtures_points/fixture_list.html'

class FixtureDetailView(DetailView):
     model = Fixture
     template_name = 'fixtures_points/fixture_detail.html'


class FixtureDeleteView(DeleteView):
    model = Fixture
    
    def get_success_url(self):
        return reverse_lazy('FixtureList')




