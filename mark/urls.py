from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.mark_view),
    path('EnterMarks', views.enter_page_view),
    path('leaderboards', views.view_leaderboard),

]
