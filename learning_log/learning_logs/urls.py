"""Defines URL schemes for learning logs"""
from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Show all topics
    path('^topics/$', views.topics, name='topics'),
    # Page with selected information on a specific topic
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Page for adding a new topic
    path('^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new record
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Post edit page
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]
