from django.db import models

import json
import urllib, urllib2

class FootballPool():
    base_url = 'http://footballpool.dataaccess.eu/data/info.wso'
    teams_raw = ''
    full_team_info_raw = { 'id' : '',
                           'data' : '' }

    def retrieve_data(self, request):
        data = urllib2.urlopen(request)
        return data

    def parse_data(self, json_data):
        return json.load(json_data)

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
