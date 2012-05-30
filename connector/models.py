from django.db import models

import json
import urllib, urllib2
from datetime import datetime

class Connector(object):
    def retrieve_data(self, request):
        data = urllib2.urlopen(request)
        return data

    def parse_data(self, json_data):
        return json.load(json_data)


class ConnectorTeam(Connector):
    base_url = 'http://footballpool.dataaccess.eu/data/info.wso'
    teams_raw = ''
    full_team_info_raw = { 'id' : '',
                           'data' : '' }

    def fetch_team_data(self):
        if self.teams_raw == '':
            req = 'http://footballpool.dataaccess.eu/data/info.wso/Teams/JSON'
            json_data = self.retrieve_data(req)
            self.teams_raw = self.parse_data(json_data)
        return  self.teams_raw

    def fetch_full_team_info(self, team_id):
        if self.full_team_info_raw['id'] != team_id:
            self.clear_full_team_info()
            team_name = self.fetch_team_item(team_id, 'name')
            params = {'sTeamName' : team_name}
            sParams = urllib.urlencode(params)
            req = 'http://footballpool.dataaccess.eu/data/info.wso/FullTeamInfo/JSON?' + sParams
            json_data = self.retrieve_data(req)
            self.full_team_info_raw = { 'id' : team_id,
                                        'data' : self.parse_data(json_data) }
        return self.full_team_info_raw['data']

    def clear_full_team_info(self):
        self.full_team_info_raw = { 'id' : '',
                                    'data' : '' }

    def fetch_team_item(self, team_id, team_data_item):
        # name, country, country_flag, info_url, coach_name
        returnValue = ''
        if team_data_item == 'name':
            returnValue =  self.fetch_team_data_item(team_id, 'sName')
        elif team_data_item == 'country':
            returnValue =  self.fetch_team_data_item(team_id, 'sName')
        elif team_data_item == 'country_flag':
            returnValue = self.fetch_team_data_item(team_id, 'sCountryFlagLarge')
        elif team_data_item == 'info_url':
            returnValue = self.fetch_team_data_item(team_id, 'sWikipediaURL')
        elif team_data_item == 'coach_name':
            returnValue = self.fetch_full_team_info_raw_item(team_id, 'sCoach')
        return returnValue

    def fetch_full_team_info_raw_item(self, team_id, key):
        full_team_info = self.fetch_full_team_info(team_id)
        full_team_info_item = full_team_info[key]
        return full_team_info_item

    def fetch_team_data_item(self, team_id, key):
        team_data = self.fetch_team_data()
        team_data_item = ''
        for team in team_data:
            if team['iId'] == team_id:
                team_data_item = team[key]
        return team_data_item

class ConnectorMatch(Connector):
    match_data_raw = { 'id' : '', 'data' : '' }
    all_matches_raw = None

    def fetch_match_data(self, match_id, match_data_item):
        match_data = []
        if match_data_item == 'description' or match_data_item == 'name':
            match_data.append(self.fetch_match_data_item(match_id, 'sDescription'))
        elif match_data_item == 'date':
            play_date = self.fetch_match_data_item(match_id, 'dPlayDate')
            play_time = self.fetch_match_data_item(match_id, 'tPlayTime')
            play_datetime = datetime.strptime(' '.join([play_date, play_time]), '%Y-%m-%d %H:%M:%S')
            match_data.append(play_datetime)
        elif match_data_item == 'team_1':
            team = self.fetch_match_data_item(match_id, 'Team1')
            match_data.append(team['iId'])
        elif match_data_item == 'team_2':
            team = self.fetch_match_data_item(match_id, 'Team2')
            match_data.append(team['iId'])
        elif match_data_item == 'score':
            match_data.append(self.fetch_match_data_item(match_id, 'sScore'))
        elif match_data_item == 'result':
            match_data.append(self.fetch_match_data_item(match_id, 'sResult'))
        elif match_data_item == 'yellow_cards':
            match_data.append(self.fetch_match_data_item(match_id, 'iYellowCards'))
        elif match_data_item == 'red_cards':
            match_data.append(self.fetch_match_data_item(match_id, 'iRedCards'))
        elif match_data_item == 'goals':
            match_data = self.fetch_match_data_item(match_id, 'Goals')
        elif match_data_item == 'cards':
            match_data = self.fetch_match_data_item(match_id, 'Cards')
        elif match_data_item == 'group':
            description = self.fetch_match_data(match_id, 'description')
            if 'Round' in description[0]:
                pass
        return match_data

    def clear_match_data_raw(self):
        self.match_data_raw = { 'id' : '', 'data' : '' }

    def fetch_game_data(self, match_id):
        if self.match_data_raw['id'] != match_id:
            self.clear_match_data_raw()
            params = {'iGameId' : match_id}
            sParams = urllib.urlencode(params)
            req = 'http://footballpool.dataaccess.eu/data/info.wso/GameInfo/JSON?' + sParams
            json_data = self.retrieve_data(req)
            self.match_data_raw = { 'id' : match_id,
                                    'data' : self.parse_data(json_data) }
        return self.match_data_raw['data']

    def fetch_match_data_item(self, match_id, key):
        if not self.all_matches_raw:
            match_data = self.fetch_game_data(match_id)
            return match_data[key]
        else:
            for match in self.all_matches_raw:
                if match['iId'] == match_id:
                    self.match_data_raw = { 'id' : match_id,
                                          'data' : match }
                    break
            match_data = self.fetch_game_data(match_id)
            return match_data[key]

    def clear_all_match_raw(self):
        self.all_matches_raw = None

    def fetch_all_match_data(self):
        if not self.all_matches_raw:
            self.clear_all_match_raw()
            req = 'http://footballpool.dataaccess.eu/data/info.wso/AllGames/JSON'
            self.all_matches_raw = self.retrieve_data(req)
        return self.all_matches_raw

if __name__ == '__main__':
    cm = ConnectorMatch()
    cm.fetch_all_match_data()
    print cm.fetch_match_data_item(7, 'description')