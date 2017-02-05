from __future__ import unicode_literals

from django.db import models
from ..users.models import User
# Create your models here.

class Message(models.Model):
	content = models.TextField(max_length=500)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	content = models.TextField(max_length=250)
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
