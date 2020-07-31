__author__ = "Yuvi"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="BlogName"),
]