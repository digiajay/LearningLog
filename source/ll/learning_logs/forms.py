from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:                 #nested Meta class informs Django about fields to include
        model = Topic           #build form from Topic model
        fields = ['text']       #incl. only text field in the form
        labels = {'text': ''}   #NO labels for text field.

