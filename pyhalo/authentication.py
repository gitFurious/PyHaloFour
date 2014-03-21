__author__ = 'Damon Pollard (@DamonLPollard)'

import re
import random
import json

import requests


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/32.0.1700.107 Safari/537.36'

SIGNIN = "https://app.halowaypoint.com/oauth/signin" \
         "?returnUrl=https%3a%2f%2fapp.halowaypoint.com%2foauth%2fspartanToken" \
         "&locale=en-US"

R_PPFT = "<input type=\"hidden\" name=\"PPFT\" id=\"i0327\" value=\"(.+?)\"\/>"
R_PPSX = "I:'(.+?)'"
R_URLPOST = "urlPost:'(.+?)'"


class HaloFour():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_new_token(self):
        s = requests.Session()

        response_one = s.get(SIGNIN,
                             headers={
                                 'user-agent': USER_AGENT,
                                 'host': 'app.halowaypoint.com'
                             },
                             allow_redirects=False
        )
        login_live_com = response_one.headers['Location']

        response_two = s.get(login_live_com,
                             headers={
                                 'user-agent': USER_AGENT,
                                 'host': 'login.live.com'
                             }
        )
        login_ppft = re.search(R_PPFT, response_two.text).group(1)
        login_ppsx = re.search(R_PPSX, response_two.text).group(1)
        urlpost = re.search(R_URLPOST, response_two.text).group(1)

        response_three = s.post(urlpost,
                                data={
                                    'PPFT': login_ppft,
                                    'login': self.username,
                                    'passwd': self.password,
                                    'LoginOptions': '3',
                                    'NewUser': '1',
                                    'PPSX': login_ppsx,
                                    'type': '11',
                                    'i3': random.randrange(5000, 10000),
                                    'm1': '1920',
                                    'm2': '1080',
                                    'm3': '0',
                                    'i12': '1',
                                    'i17': '0',
                                    'i18': '__MobileLogin|1,',
                                },
                                headers={
                                    'user-agent': USER_AGENT,
                                    'referer': login_live_com,
                                    'host': 'login.live.com',
                                    'origin': 'https://login.live.com'
                                },
                                verify=False,
                                allow_redirects=False
        )
        callback_url = response_three.headers['Location']

        response_four = s.get(callback_url,
                              headers={
                                  'user-agent': USER_AGENT,
                                  'referer': login_live_com,
                                  'host': 'www.halowaypoint.com'
                              },
                              verify=False,
                              allow_redirects=False
        )
        spartantoken_url = response_four.headers['Location']

        response_five = s.get(spartantoken_url,
                              headers={
                                  'user-agent': USER_AGENT,
                                  'referer': login_live_com,
                                  'host': 'app.halowaypoint.com'
                              },
                              verify=False
        )
        j = json.loads(response_five.text)

        return self.WaypointToken(j['SpartanToken'], j['Gamertag'], j['AnalyticsToken'])

    class WaypointToken:
        def __init__(self, spartan_token, gamertag, analytics_token):
            self.spartan_token = spartan_token
            self.gamertag = gamertag
            self.analytics_token = analytics_token
