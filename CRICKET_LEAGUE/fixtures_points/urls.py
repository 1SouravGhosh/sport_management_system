from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('group/create', views.GroupCreateView.as_view(),name='GroupCreate'),
    path('group/update/<int:pk>', views.GroupUpdateView.as_view(),name='GroupUpdate'),
    path('group/delete/<int:pk>', views.GroupDeleteView.as_view(),name='GroupDelete'),
    path('group/list', views.GroupListView.as_view(),name='GroupList'), 
    
    path('create', views.FixtureCreateView.as_view(),name='FixtureCreate'),
    path('update/<int:pk>', views.FixtureUpdateView.as_view(),name='FixtureUpdate'),
    path('<int:pk>', views.FixtureDetailView.as_view(),name='FixtureDetail'),
    path('delete/<int:pk>', views.FixtureDeleteView.as_view(),name='FixtureDelete'),
    path('list', views.FixtureListView.as_view(),name='FixtureList'),
]
