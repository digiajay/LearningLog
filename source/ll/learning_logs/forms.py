from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:                 #nested Meta class informs Django about fields to include
        model = Topic           #build form from Topic model
        fields = ['topic']       #incl. only text field in the form
        labels = {'topic': 'Enter Topic'}   #NO labels for text field.

