from django.db import models
from ..auth.models import User
from ..words.models import Word
from ..turns.models import Turn


# TODO CWS: Could this be a data structure with cheap insert and cheap read?
class Rank(models.Model):
    order = models.CharField(max_length=63)
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    turn = models.ForeignKey(Turn)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
