from django.utils import unittest
from connector.models import ConnectorTeam

class FootballPoolTestCase(unittest.TestCase):
    def setUp(self):
        self.ct = ConnectorTeam()

    def test_connector_can_fetch_team_info(self):
        """Connector can fetch correct team info"""
        self.assertEqual(self.ct.fetch_team_item(7, 'name'), 'Germany')
        self.assertEqual(self.ct.fetch_team_item(7, 'country'), 'Germany')
        self.assertEqual(self.ct.fetch_team_item(7, 'country_flag'), 'http://footballpool.dataaccess.eu/images/flags/de.png')
        self.assertEqual(self.ct.fetch_team_item(7, 'info_url'), 'http://en.wikipedia.org/wiki/Germany_national_football_team')
        self.assertEqual(self.ct.fetch_team_item(7, 'coach_name'), u'Joachim L\xf6w')

        self.assertEqual(self.ct.fetch_team_item(7, 'name'), 'Germany')
        self.assertEqual(self.ct.fetch_team_item(7, 'country'), 'Germany')
        self.assertEqual(self.ct.fetch_team_item(7, 'country_flag'), 'http://footballpool.dataaccess.eu/images/flags/de.png')
        self.assertEqual(self.ct.fetch_team_item(7, 'info_url'), 'http://en.wikipedia.org/wiki/Germany_national_football_team')
        self.assertEqual(self.ct.fetch_team_item(7, 'coach_name'), u'Joachim L\xf6w')

        self.assertEqual(self.ct.fetch_team_item(9, 'name'), 'Spain')
        self.assertEqual(self.ct.fetch_team_item(9, 'country'), 'Spain')
        self.assertEqual(self.ct.fetch_team_item(9, 'country_flag'), 'http://footballpool.dataaccess.eu/images/flags/es.png')
        self.assertEqual(self.ct.fetch_team_item(9, 'info_url'), 'http://en.wikipedia.org/wiki/Spain_national_football_team')
        self.assertEqual(self.ct.fetch_team_item(9, 'coach_name'), u'Vicente del Bosque')

