from django.shortcuts import redirect, render

from .forms import TopicForm
from .models import Topic

# Create your views here.
def index(request):
    '''Homepage for Learning Log'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics added so far"""
    topics = Topic.objects.order_by('timestamp_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """Show a single topic and all it's entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-timestamp_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        #No data submitted; so create a blank form.
        form = TopicForm()
    else:
        #POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    #display a blank form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html',context)