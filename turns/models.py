from django.db import models
from ..auth.models import User
from ..games.models import Game


# TODO CWS: Could this be a data structure with cheap insert and cheap read?
class Turn(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    created_at = models.DateTimeField(auto_now_add=True)
