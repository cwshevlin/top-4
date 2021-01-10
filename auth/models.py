from django.contrib.auth.models import AbstractUser
from django.db import models
from ..games.models import Game


class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    # URLField: default max length is 200
    avatar_url = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=128, null=True)
    is_superuser = models.BooleanField(default=False)

    users = models.ManyToManyField(Game)

    # Only affects creation of a user from the createsuperuser method, not from any other part of the app.
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
