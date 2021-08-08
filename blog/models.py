from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Library(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library-detail', kwargs={'pk': self.pk})


class Post(models.Model):
    def get_library_choices():
        choices =  Library.objects.values('name')
        choice = [(d['name'], d['name']) for d in choices]
        return choice

    title = models.CharField(max_length=100)
    library = models.CharField(max_length=250, choices=get_library_choices(), default='Null')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})