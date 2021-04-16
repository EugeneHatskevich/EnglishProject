from django.shortcuts import render
from .models import Topics


def view_all_topics(request):
    all_topics = {'topics': Topics.objects.all()}
    return render(request, 'topics/index.html', all_topics)


def view_topic(request, topic_id):
    topic = Topics.objects.get(topic_id=topic_id)
    return render(request, 'topics/ghgjh.html', {'topic':topic})
