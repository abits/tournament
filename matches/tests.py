from matches.models import Team
from connector.models import ConnectorTeam

from django.test import TestCase


class MatchesTest(TestCase):
    def setUp(self):
        self.testTeam = Team()
        self.testConnector = ConnectorTeam()

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

#    def test_get_team_data(self):
#        testTeam7 = Team.objects.get_or_create(id=7)
#        self.assertEqual(testTeam7.name, self.testConnector.fetch_team_item(testTeam7.id, 'name'))
#        self.assertEqual(testTeam7.country, self.testConnector.fetch_team_item(testTeam7.id, 'country'))
#        self.assertEqual(testTeam7.country_flag, self.testConnector.fetch_team_item(testTeam7.id, 'country_flag'))
#        self.assertEqual(testTeam7.info_url, self.testConnector.fetch_team_item(testTeam7.id, 'info_url'))
#        self.assertEqual(testTeam7.coach_name, self.testConnector.fetch_team_item(testTeam7.id, 'coach_name'))
#

