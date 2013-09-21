from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	goal = models.IntegerField()
	current = models.IntegerField()
	deadline = models.DateTimeField()
	created_by = models.ForeignKey(User, unique=True)

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	email = models.EmailField()
	events = models.ManyToManyField(Event)