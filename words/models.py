from django.db import models
from ..auth.models import User
from ..games.models import Game
from ..games.models import Turn


# TODO CWS: Could this be a data structure with cheap insert and cheap read?
class Word(models.Model):
    creator = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    value = models.CharField(max_length=255)
    last_turn_used = models.ForeignKey(Turn)
    created_at = models.DateTimeField(auto_now_add=True)
