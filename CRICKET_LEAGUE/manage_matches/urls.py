from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:pk>', views.MatchDetailView.as_view(),name='MatchDetail'),
    path('list', views.MatchListView.as_view(),name='MatchList'), 
    path('pointlist', views.PointListView.as_view(),name='Pointlist'), 
]
