import json
import urllib, urllib2


class FootballPool():
    base_url = 'http://footballpool.dataaccess.eu/data/info.wso'

    def retrieve_data(self):
        request = self.base_url + '/AllGames' + '/JSON'
        data = urllib2.urlopen(request)
        return data

    def parse_data(self, json_data):
        return json.load(json_data)

if __name__ == '__main__':
    test_driver = FootballPool()
    data = test_driver.retrieve_data()
    parsed_data = test_driver.parse_data(data)
    for match in parsed_data:
        print match['Team1']