from django.urls import path
from . import views

urlpatterns = [
    path('', views.puzzle_view, name='puzzle_view'),
]
