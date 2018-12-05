import unittest
import requests


class TestTeamEndpoint(unittest.TestCase):

    def setUp(self):
        # Put the url (without /api/...) you want to run the tests on here:
        # Tests shouldn't affect the database but could if an error occurs in the right place.
        self.url = 'https://dev.frederictonfootball.me'

        r = requests.post(self.url + '/api/login',
                          data={'email': 'admin@site.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the admin test account.")
        else:
            self.adminToken = r.json()['token']

        r = requests.post(self.url + '/api/login',
                          data={'email': 'coordinator@league.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the coordinator test account.")
        else:
            self.coordinatorToken = r.json()['token']

        r = requests.post(self.url + '/api/login',
                          data={'email': 'manager@team.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the manager test account.")
        else:
            self.managerToken = r.json()['token']

        r = requests.post(self.url + '/api/login',
                          data={'email': 'referee@league.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the referee test account.")
        else:
            self.refereeToken = r.json()['token']

        r = requests.post(self.url + '/api/login',
                          data={'email': 'user@default.ca', 'password': 'password'})
        if r.status_code != 201:
            raise ValueError("Could not log in to the default user test account.")
        else:
            self.userToken = r.json()['token']

    def test_get(self):
        r = requests.get(self.url + '/api/team')
        self.assertEqual(r.status_code, 200)

    def test_postNoToken(self):
        r = requests.post(self.url + '/api/team',
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 403)

    def test_postAdmin(self):
        r = requests.post(self.url + '/api/team',
                          headers={'Authorization': self.adminToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 201)

    def test_postCoodrinator(self):
        r = requests.post(self.url + '/api/team',
                          headers={'Authorization': self.coordinatorToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 201)

    def test_postManager(self):
        r = requests.post(self.url + '/api/team',
                          headers={'Authorization': self.managerToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 201)

    def test_postReferee(self):
        r = requests.post(self.url + '/api/team',
                          headers={'Authorization': self.refereeToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 403)

    def test_postUser(self):
        r = requests.post(self.url + '/api/team',
                          headers={'Authorization': self.userToken},
                          data={'teamName': 'TEST TEAM', 'leagueID': 1, 'colour': 'ABCDEF'})
        self.assertEqual(r.status_code, 403)

    def put_NoToken(self):
        r = requests.get(self.url + '/api/team')
        team = r.json()['teams'][0]

        r2 = requests.put(self.url + '/api/team',
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'] + ' TEST EDIT',
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r2.status_code, 403)

    def test_putAdmin(self):
        r = requests.get(self.url + '/api/team')
        team = r.json()['teams'][0]

        r2 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.adminToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'] + ' TEST EDIT',
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r2.status_code, 200)

        r3 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.adminToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'],
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r3.status_code, 200)

    def test_putCoodrinator(self):
        r = requests.get(self.url + '/api/team')
        team = r.json()['teams'][0]

        r2 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.coordinatorToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'] + ' TEST EDIT',
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r2.status_code, 200)

        r3 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.coordinatorToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'],
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r3.status_code, 200)

    def test_putManager(self):
        r = requests.get(self.url + '/api/team')
        team = r.json()['teams'][0]

        r2 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.managerToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'] + ' TEST EDIT',
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r2.status_code, 200)

        r3 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.managerToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'],
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r3.status_code, 200)

    def test_putReferee(self):
        r = requests.get(self.url + '/api/team')
        team = r.json()['teams'][0]

        r2 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.refereeToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'] + ' TEST EDIT',
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r2.status_code, 403)

    def test_putUser(self):
        r = requests.get(self.url + '/api/team')
        team = r.json()['teams'][0]

        r2 = requests.put(self.url + '/api/team',
                          headers={'Authorization': self.userToken},
                          data={'teamID': team['teamID'],
                                'leagueID': team['leagueID'],
                                'managerID': team['managerID'],
                                'teamName': team['teamName'] + ' TEST EDIT',
                                'colour': team['colour'],
                                'leaguePoints': team['leaguePoints'],
                                'wins': team['wins'],
                                'losses': team['losses'],
                                'draws': team['draws']})
        self.assertEqual(r2.status_code, 403)

    def test_delete(self):
        r = requests.get(self.url + '/api/team')
        for team in r.json()['teams']:
            if team['teamName'] == 'TEST TEAM':
                # No token
                r0 = requests.delete(self.url + '/api/team',
                                     data={'teamID': team['teamID']})
                self.assertEqual(r0.status_code, 403)
                # Default user
                r1 = requests.delete(self.url + '/api/team',
                                     data={'teamID': team['teamID']},
                                     headers={'Authorization': self.userToken})
                self.assertEqual(r1.status_code, 403)
                # Admin
                r2 = requests.delete(self.url + '/api/team',
                                     data={'teamID': team['teamID']},
                                     headers={'Authorization': self.adminToken})
                self.assertEqual(r2.status_code, 200)

    def tearDown(self):
        r = requests.get(self.url + '/api/team')
        for team in r.json()['teams']:
            if team['teamName'] == 'TEST TEAM':
                r2 = requests.delete(self.url + '/api/team',
                                     data={'teamID': team['teamID']},
                                     headers={'Authorization': self.adminToken})
                if r2.status_code != 200:
                    raise ValueError('Team tests failed to clean up the database due to a failed delete request (code '
                                     + r2.status_code + ')')
            else:
                index = team['teamName'].find(' TEST EDIT')
                team['teamName'] = team['teamName'][0:index]
                r3 = requests.put(self.url + '/api/team',
                                  headers={'Authorization': self.adminToken},
                                  data={'teamID': team['teamID'],
                                        'leagueID': team['leagueID'],
                                        'managerID': team['managerID'],
                                        'teamName': team['teamName'],
                                        'colour': team['colour'],
                                        'leaguePoints': team['leaguePoints'],
                                        'wins': team['wins'],
                                        'losses': team['losses'],
                                        'draws': team['draws']})
                if r3.status_code != 200:
                    raise ValueError('Team tests failed to clean up the database due to a failed put request (code '
                                     + r3.status_code + ')')


if __name__ == '__main__':
    unittest.main()
