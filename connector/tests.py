from django.utils import unittest
from connector.footballpool import FootballPool

class FootballPoolTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = FootballPool()

    def test_connector_can_fetch_team_info(self):
        """Connector can fetch correct team info"""
        self.assertEqual(self.fp.fetch_team_item(7, 'name'), 'Germany')
        self.assertEqual(self.fp.fetch_team_item(7, 'country'), 'Germany')
        self.assertEqual(self.fp.fetch_team_item(7, 'country_flag'), 'http://footballpool.dataaccess.eu/images/flags/de.png')
        self.assertEqual(self.fp.fetch_team_item(7, 'info_url'), 'http://en.wikipedia.org/wiki/Germany_national_football_team')
        self.assertEqual(self.fp.fetch_team_item(7, 'coach_name'), 'Joachim Löw')

        self.assertEqual(self.fp.fetch_team_item(7, 'name'), 'Germany')
        self.assertEqual(self.fp.fetch_team_item(7, 'country'), 'Germany')
        self.assertEqual(self.fp.fetch_team_item(7, 'country_flag'), 'http://footballpool.dataaccess.eu/images/flags/de.png')
        self.assertEqual(self.fp.fetch_team_item(7, 'info_url'), 'http://en.wikipedia.org/wiki/Germany_national_football_team')
        self.assertEqual(self.fp.fetch_team_item(7, 'coach_name'), 'Joachim Löw')

        self.assertEqual(self.fp.fetch_team_item(9, 'name'), 'Spain')
        self.assertEqual(self.fp.fetch_team_item(9, 'country'), 'Spain')
        self.assertEqual(self.fp.fetch_team_item(9, 'country_flag'), 'http://footballpool.dataaccess.eu/images/flags/es.png')
        self.assertEqual(self.fp.fetch_team_item(9, 'info_url'), 'http://en.wikipedia.org/wiki/Spain_national_football_team')
        self.assertEqual(self.fp.fetch_team_item(9, 'coach_name'), 'Vicente del Bosque')

