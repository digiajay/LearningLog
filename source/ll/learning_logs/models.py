from django.db import models

# Create your models here.

class Topic(models.Model):
    #Tell Django to manage the data associated with the topic here
    topic = models.CharField(max_length=100)

    timestamp_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return string representation of model'''
        return self.topic

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()

    timestamp_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.text[:50]}..."
    