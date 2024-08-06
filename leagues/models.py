from django.db import models
from django.utils.text import slugify

from events.models import Event

class League(Event):
    start_date = models.DateTimeField()
    num_games = models.PositiveIntegerField(default=3)