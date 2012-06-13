from django.db import models
from django.contrib.auth.models import User
from connector.models import ConnectorMatch, ConnectorTeam
from datetime import datetime, timedelta
import json


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
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
    team_1 = models.ForeignKey(Team, related_name='team_1', null=True)
    team_2 = models.ForeignKey(Team, related_name='team_2', null=True)
    winner = models.ForeignKey(Team, related_name='winner', blank=True, null=True)
    score_1 = models.IntegerField(max_length=2, blank=True, null=True)
    score_2 = models.IntegerField(max_length=2, blank=True, null=True)
    result = models.CharField(max_length=8, blank=True)
    yellow_cards = models.IntegerField(max_length=2, blank=True, null=True)
    red_cards = models.IntegerField(max_length=2, blank=True, null=True)
    goals = models.CharField(max_length=65536, blank=True)
    cards = models.CharField(max_length=65536, blank=True)
    users = models.ManyToManyField(User, through='Bet', blank=True, null=True)
    level = models.IntegerField(max_length=2, blank=True, null=True)
    group = models.CharField(max_length=1, blank=True)

    def get_score(self, team=None):
        score = ''
        if self.result != 'U':
            score = self.score.replace('-', ' : ')
        if (team is not None) and score:
            scores = score.split('-')
            index = team - 1
            return scores[index]
        else:
            return score

    def get_score_1(self):
        return self.get_score(1)

    def get_score_2(self):
        return self.get_score(2)

    def is_locked(self):
        return bool(self.date < (datetime.now() - timedelta(minutes=15)))


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

class Tournament(object):
    """
    Creates database information for a tournament.
    .. note::
        `Uses the borg pattern instead of singleton. <http://code.activestate.com/recipes/66531/>`
    """
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

    def initialize(self):
        """Persist initial tournament info."""
        self.initialize_teams()
        self.initialize_matches()

    def initialize_teams(self):
        ct = ConnectorTeam()
        for ct_team in ct.fetch_team_data():
            team = Team()
            team.id = ct_team['iId']
            team.name = ct.fetch_team_item(team.id, 'name')
            team.country = ct.fetch_team_item(team.id, 'country')
            team.country_flag = ct.fetch_team_item(team.id, 'country_flag')
            team.info_url = ct.fetch_team_item(team.id, 'info_url')
            team.coach_name = ct.fetch_team_item(team.id, 'coach_name')
            team.save()

    def initialize_matches(self):
        cm = ConnectorMatch()
        for cm_match in cm.fetch_all_match_data():
            match = Match()
            match.id = cm_match['iId']
            match.name = cm.fetch_match_data(match.id, 'name')
            match.date = cm.fetch_match_data(match.id, 'date')
            try:
                team_1 = Team.objects.get(id=cm.fetch_match_data(match.id, 'team_1'))
                match.team_1 = team_1
            except Team.DoesNotExist:
                match.team_1 = None
            try:
                team_2 = Team.objects.get(id=cm.fetch_match_data(match.id, 'team_2'))
                match.team_2 = team_2
            except Team.DoesNotExist:
                match.team_2= None
            match.cards = json.dumps(cm.fetch_match_data(match.id, 'cards'))
            match.description = cm.fetch_match_data(match.id, 'description')
            match.group = cm.fetch_match_data(match.id, 'group')
            match.score = cm.fetch_match_data(match.id, 'score')
            match.goals = json.dumps(cm.fetch_match_data(match.id, 'goals'))
            match.result = cm.fetch_match_data(match.id, 'result')
            match.red_cards = json.dumps(cm.fetch_match_data(match.id, 'red_cards'))
            match.yellow_cards = json.dumps(cm.fetch_match_data(match.id, 'yellow_cards'))
            match.save()

    def schedule(self):

        pass


