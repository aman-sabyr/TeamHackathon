from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

User = get_user_model()


class Chat(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    people = ArrayField(models.ForeignKey(User, on_delete=models.RESTRICT))
    created_at = models.DateTimeField()
    avatar = models.FileField()
