from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index),
    path('instructions/', views.instructions),
    path('puzzle/<int:puzzleId>/', views.puzzle),
    path('pdf/<int:puzzleId>/', views.puzzlePDF),
    path('puzzles/', views.puzzles),
    path('solve/<int:puzzleId>/', views.solve),
    path('leaderboard/', views.leaderboard),
    path('announcements/', views.announcements),
    path('wardle/<str:wardleId>/', views.wardle),
]
