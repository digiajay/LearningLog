"Define URL patterns for learning_logs"

from unicodedata import name
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    path('topics',views.topics,name='topics'),

    #topic id association with path.
    path('topics/<int:topic_id>/',views.topic,name='topic'),

    #page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #page for adding new entry
    path('new_entry/<int:topic_id>',views.new_entry, name='new_entry'),

    #page for editing entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]