from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create', views.PlayerCreateView.as_view(),name='PlayerCreate'),
    path('update/<int:pk>', views.PlayerUpdateView.as_view(),name='PlayerUpdate'),
    path('<int:pk>', views.PlayerDetailView.as_view(),name='PlayerDetail'),
    path('delete/<int:pk>', views.PlayerDeleteView.as_view(),name='PlayerDelete'),
    path('list', views.PlayerListView.as_view(),name='PlayerList'), 
]
