from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('matches/<int:pk>', views.MatchDetailView.as_view(),name='MatchDetail'),
    path('matches/list', views.MatchListView.as_view(),name='MatchList'), 
    path('pointlist', views.PointListView.as_view(),name='Pointlist'),  
    path('', views.home,name='HomePage'), 
]
