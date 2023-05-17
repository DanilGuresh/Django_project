"""Defines URL schemes for learning logs"""
from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Show all topics
    path('topics/', views.topics, name='topics'),
    # Page with selected information on a specific topic
    path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic')
]
