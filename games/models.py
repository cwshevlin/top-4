from django.db import models
from ..auth.models import User


class Game(models.Model):
    code = models.CharField(max_length=63)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

