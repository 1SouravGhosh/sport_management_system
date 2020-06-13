from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from .models import Fixture
from .forms import FixtureDetailForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

class FixtureCreateView(CreateView):
    model = Fixture
    form_class = FixtureDetailForm
    template_name = 'manage_Fixtures/fixture_create_update.html'

    def get_success_url(self):
        return reverse('FixtureList')


class FixtureUpdateView(UpdateView):
    model = Fixture
    form_class = FixtureDetailForm
    template_name = 'manage_Fixtures/fixture_create_update.html'
    
    def get_success_url(self):
        return reverse('FixtureDetail',kwargs={'pk': self.object.identifier})


class FixtureListView(ListView):
    model = Fixture
    template_name = 'manage_Fixtures/fixture_list.html'

class FixtureDetailView(DetailView):
    model = Fixture
    template_name = 'manage_Fixtures/fixture_detail.html'


class FixtureDeleteView(DeleteView):
    model = Fixture
    def get_success_url(self):
        return reverse_lazy('FixtureList')

