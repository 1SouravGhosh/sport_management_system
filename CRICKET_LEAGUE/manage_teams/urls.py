from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create', views.TeamCreateView.as_view(),name='TeamCreate'),
    path('update/<int:pk>', views.TeamUpdateView.as_view(),name='TeamUpdate'),
    path('<int:pk>', views.TeamDetailView.as_view(),name='TeamDetail'),
    path('delete/<int:pk>', views.TeamDeleteView.as_view(),name='TeamDelete'),
    path('list', views.TeamListView.as_view(),name='TeamList'), 
]
