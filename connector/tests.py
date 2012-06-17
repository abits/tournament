from django.utils import unittest
from connector.models import ConnectorTeam, ConnectorMatch
from datetime import datetime

class FootballPoolTestCase(unittest.TestCase):
    def setUp(self):
        self.ct = ConnectorTeam()
        self.cm = ConnectorMatch()
        self.cm.fetch_all_match_data()
       # for match in self.cm.all_matches_raw: print match

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

    def test_connector_can_fetch_match_info(self):
        """Connector can fetch match info"""
        self.assertEqual(self.cm.fetch_match_data(17, 'description'), [u'Round 3'])
        self.assertEqual(self.cm.fetch_match_data(17, 'result'), [u'U'])
        self.assertEqual(self.cm.fetch_match_data(17, 'score_1'), [1])
        self.assertEqual(self.cm.fetch_match_data(17, 'score_2'), [0])
        self.assertEqual(self.cm.fetch_match_data(17, 'yellow_cards'), [0])
        self.assertEqual(self.cm.fetch_match_data(17, 'red_cards'), [0])
        self.assertEqual(self.cm.fetch_match_data(17, 'team_1'), [4])
        self.assertEqual(self.cm.fetch_match_data(17, 'team_2'), [1])
        self.assertEqual(self.cm.fetch_match_data(17, 'date'), [datetime(2012, 06, 16, 20, 45, 00)])

        self.assertEqual(self.cm.fetch_match_data(3, 'description'), [u'Round 1'])
        self.assertEqual(self.cm.fetch_match_data(3, 'result'), [u'U'])
        self.assertEqual(self.cm.fetch_match_data(17, 'score_1'), [1])
        self.assertEqual(self.cm.fetch_match_data(17, 'score_2'), [0])
        self.assertEqual(self.cm.fetch_match_data(3, 'yellow_cards'), [0])
        self.assertEqual(self.cm.fetch_match_data(3, 'red_cards'), [0])
        self.assertEqual(self.cm.fetch_match_data(3, 'team_1'), [5])
        self.assertEqual(self.cm.fetch_match_data(3, 'team_2'), [6])
        self.assertEqual(self.cm.fetch_match_data(3, 'date'), [datetime(2012, 06, 9, 18, 00, 00)])

        self.assertEqual(self.cm.fetch_match_data(3, 'description'), [u'Round 1'])
        self.assertEqual(self.cm.fetch_match_data(3, 'result'), [u'U'])
        self.assertEqual(self.cm.fetch_match_data(17, 'score_1'), [1])
        self.assertEqual(self.cm.fetch_match_data(17, 'score_2'), [0])
        self.assertEqual(self.cm.fetch_match_data(3, 'yellow_cards'), [0])
        self.assertEqual(self.cm.fetch_match_data(3, 'red_cards'), [0])
        self.assertEqual(self.cm.fetch_match_data(3, 'team_1'), [5])
        self.assertEqual(self.cm.fetch_match_data(3, 'team_2'), [6])
        self.assertEqual(self.cm.fetch_match_data(3, 'date'), [datetime(2012, 06, 9, 18, 00, 00)])
