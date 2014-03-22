__author__ = 'Damon Pollard (@DamonLPollard)'

import re
import random

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
    """ Class for retrieving a Halo Waypoint Token (required to authenticate with the Halo Waypoint API)
        allow_redirects is False where applicable in order to not disguise Location Header redirects.
    """

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
        oauth20_authorize = response_one.headers['Location']

        response_two = s.get(oauth20_authorize,
                             headers={
                                 'user-agent': USER_AGENT,
                                 'host': 'login.live.com'
                             }
        )
        ppft = re.search(R_PPFT, response_two.text).group(1)
        ppsx = re.search(R_PPSX, response_two.text).group(1)
        urlpost = re.search(R_URLPOST, response_two.text).group(1)

        response_three = s.post(urlpost,
                                data={
                                    'PPFT': ppft,
                                    'login': self.username,
                                    'passwd': self.password,
                                    'LoginOptions': '3',
                                    'NewUser': '1',
                                    'PPSX': ppsx,
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
                                    'referer': oauth20_authorize,
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
                                  'referer': oauth20_authorize,
                                  'host': 'www.halowaypoint.com'
                              },
                              verify=False,
                              allow_redirects=False
        )
        spartantoken_url = response_four.headers['Location']

        response_five = s.get(spartantoken_url,
                              headers={
                                  'user-agent': USER_AGENT,
                                  'referer': oauth20_authorize,
                                  'host': 'app.halowaypoint.com'
                              },
                              verify=False
        )
        j = response_five.json()

        return self.HaloWaypointToken(j['SpartanToken'],
                                      j['Gamertag'],
                                      j['AnalyticsToken'],
                                      self.username,
                                      self.password
        )

    class HaloWaypointToken:
        def __init__(self, spartan_token, gamertag, analytics_token, live_username, live_password):
            self.spartan_token = spartan_token
            self.gamertag = gamertag
            self.analytics_token = analytics_token
            self.live_username = live_username
            self.live_password = live_password
