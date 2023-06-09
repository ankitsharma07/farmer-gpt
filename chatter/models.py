from django.db import models


class Message(models.Model):
    content = models.TextField()
    is_user = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)