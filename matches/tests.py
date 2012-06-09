from matches.models import Team, Tournament
from connector.models import ConnectorTeam

from django.test import TestCase


class MatchesTest(TestCase):
    def setUp(self):
        self.testTeam = Team()
        self.testConnector = ConnectorTeam()
        self.testTournament = Tournament()

    def test_create_team(self):
        self.assertIsInstance(self.testTeam, Team)

    def test_update_team(self):
        self.testTeam.id = 7
        self.testTeam.name = self.testConnector.fetch_team_item(self.testTeam.id, 'name')
        self.testTeam.country = self.testConnector.fetch_team_item(self.testTeam.id, 'country')
        self.testTeam.country_flag = self.testConnector.fetch_team_item(self.testTeam.id, 'country_flag')
        self.testTeam.info_url = self.testConnector.fetch_team_item(self.testTeam.id, 'info_url')
        self.testTeam.coach_name = self.testConnector.fetch_team_item(self.testTeam.id, 'coach_name')
        self.testTeam.save()

    def test_initialize(self):
        self.testTournament.initialize_teams()
        self.testTournament.initialize_matches()
