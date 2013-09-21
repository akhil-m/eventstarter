from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Event(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	goal = models.IntegerField(default=0)
	current = models.IntegerField()
	deadline = models.DateTimeField()
	created_by = models.ForeignKey(User, unique=True, default=1)

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'description', 'goal', 'deadline']

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	email = models.EmailField()
	events = models.ManyToManyField(Event)