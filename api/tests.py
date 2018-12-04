import unittest
import requests


class TestTeamEndpoint(unittest.TestCase):

    def setUp(self):
        r = requests.post('https://dev.frederictonfootball.me/api/login',
                          data={'email': 'admin@site.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the admin test account.")
        else:
            self.adminToken = r.json()['token']

        r = requests.post('https://dev.frederictonfootball.me/api/login',
                          data={'email': 'coordinator@league.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the coordinator test account.")
        else:
            self.coordinatorToken = r.json()['token']

        r = requests.post('https://dev.frederictonfootball.me/api/login',
                          data={'email': 'manager@team.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the manager test account.")
        else:
            self.managerToken = r.json()['token']

        r = requests.post('https://dev.frederictonfootball.me/api/login',
                          data={'email': 'referee@league.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the referee test account.")
        else:
            self.refereeToken = r.json()['token']

        r = requests.post('https://dev.frederictonfootball.me/api/login',
                          data={'email': 'user@default.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the default user test account.")
        else:
            self.userToken = r.json()['token']

    def test_get(self):
        r = requests.get('https://dev.frederictonfootball.me/api/team')
        self.assertEqual(r.status_code, 200)

    def test_postNoToken(self):
        r = requests.post('https://dev.frederictonfootball.me/api/team',
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 403)

    def test_postAdmin(self):
        r = requests.post('https://dev.frederictonfootball.me/api/team',
                          headers={'Authorization': self.adminToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 201)

    def test_postCoodrinator(self):
        r = requests.post('https://dev.frederictonfootball.me/api/team',
                          headers={'Authorization': self.coordinatorToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 201)

    def test_postManager(self):
        r = requests.post('https://dev.frederictonfootball.me/api/team',
                          headers={'Authorization': self.managerToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 201)

    def test_postReferee(self):
        r = requests.post('https://dev.frederictonfootball.me/api/team',
                          headers={'Authorization': self.refereeToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 403)

    def test_postUser(self):
        r = requests.post('https://dev.frederictonfootball.me/api/team',
                          headers={'Authorization': self.userToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 403)

    def test_putNoToken(self):
        self.assertEqual(True, True)

    def test_postAdmin(self):
        self.assertEqual(True, True)

    def test_postCoodrinator(self):
        self.assertEqual(True, True)

    def test_postManager(self):
        self.assertEqual(True, True)

    def test_postReferee(self):
        self.assertEqual(True, True)

    def test_postUser(self):
        self.assertEqual(True, True)

    def test_delete(self):
        r = requests.get('https://dev.frederictonfootball.me/api/team')
        for team in r.json()['teams']:
            if team['teamName'] == 'TEST TEAM':
                r2 = requests.delete('https://dev.frederictonfootball.me/api/team',
                                     data={'teamID': team['teamID']},
                                     headers={'Authorization': self.adminToken})
                self.assertEqual(r2.status_code, 200)

    def tearDown(self):
        r = requests.get('https://dev.frederictonfootball.me/api/team')
        for team in r.json()['teams']:
            if team['teamName'] == 'TEST TEAM':
                r2 = requests.delete('https://dev.frederictonfootball.me/api/team',
                                     data={'teamID': team['teamID']},
                                     headers={'Authorization': self.adminToken})


if __name__ == '__main__':
    unittest.main()
