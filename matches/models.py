from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=128, blank=True)
    country_flag = models.URLField(blank=True)
    info_url = models.URLField(blank=True)
    coach_name = models.CharField(max_length=128)
    matches_won = models.IntegerField(max_length=2, null=True)
    matches_lost = models.IntegerField(max_length=2, null=True)
    matches_played = models.IntegerField(max_length=2, null=True)

class Match(models.Model):
    name = models.CharField(max_length=128, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    date = models.DateTimeField(blank=False)
    team_1 = models.ForeignKey(Team, related_name='team_1')
    team_2 = models.ForeignKey(Team, related_name='team_2')
    winner = models.ForeignKey(Team, related_name='winner')
    score = models.CharField(max_length=8, blank=True)
    result = models.CharField(max_length=8, blank=True)
    yellow_cards = models.IntegerField(max_length=2, blank=True, null=True)
    red_cards = models.IntegerField(max_length=2, blank=True, null=True)
    goals = models.CharField(max_length=1024, blank=True)
    cards = models.CharField(max_length=1024, blank=True)
    users = models.ManyToManyField(User, through='Bet')
    level = models.IntegerField(max_length=2)
    group = models.CharField(max_length=1, blank=True)

class Bet(models.Model):
    stake = models.CharField(max_length=128, blank=True)
    result = models.CharField(max_length=8, blank=True)
    user = models.ForeignKey(User)
    match = models.ForeignKey(Match)
    date_placed = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)

class Stadium(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    seats_capacity = models.IntegerField(max_length=6)
    map_url = models.URLField(blank=True)
    info_url = models.URLField(blank=True)

class Player(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team)
    position = models.CharField(max_length=12)
    goals = models.IntegerField(max_length=3, default=0)
    yellow_cards = models.IntegerField(max_length=2, blank=True, null=True)
    red_cards = models.IntegerField(max_length=2, blank=True, null=True)


