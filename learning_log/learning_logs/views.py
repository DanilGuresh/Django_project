from django.shortcuts import render
from .models import Topic


def index(request):
    """Home page of the Learning Log app"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Displays a list of topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Displays one topic and all of its posts"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topics': topics, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
