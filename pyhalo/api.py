__author__ = 'Damon Pollard (@DamonLPollard)'

import requests


class HaloFour():
    def __init__(self, waypoint_token):
        self.waypoint_token = waypoint_token

    def get_api_version(self):
        url = "https://app.halowaypoint.com/en-US/home/version"
        return self._fetch_json(url)

    def get_api_services(self):
        url = "https://settings.svc.halowaypoint.com/RegisterClientService.svc" \
              "/register/webapp/AE5D20DCFA0347B1BCE0A5253D116752"
        return self._fetch_json(url)

    def get_user_achievements(self, params):
        url = "https://haloplayer.svc.halowaypoint.com/HaloPlayer/GetOtherUserAchievements"
        return self._fetch_json(url, params)

    def get_playlists(self):
        url = "https://presence.svc.halowaypoint.com/en-US/h4/playlists"
        return self._fetch_json(url)

    def get_global_challenges(self):
        url = "https://stats.svc.halowaypoint.com/en-US/h4/challenges"
        return self._fetch_json(url)

    def get_player_challenges(self):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/challenges" % self.waypoint_token.gamertag
        return self._fetch_json(url)

    def get_game_metadata(self, params=None):
        url = "https://stats.svc.halowaypoint.com/en-US/h4/metadata"
        return self._fetch_json(url, params)

    def get_playercard(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/playercard" % gamertag
        return self._fetch_json(url)

    def get_multiple_playercards(self, params):
        url = "https://stats.svc.halowaypoint.com/en-US/h4/playercards"
        return self._fetch_json(url, params)

    def get_service_record(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/servicerecord" % gamertag
        return self._fetch_json(url)

    def get_game_history(self, gamertag, params=None):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/matches" % gamertag
        return self._fetch_json(url, params)

    def get_game_details(self, game_id):
        url = "https://stats.svc.halowaypoint.com/en-US/h4/matches/%s" % game_id
        return self._fetch_json(url)

    def get_commendations(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/commendations" % gamertag
        return self._fetch_json(url)

    # HTTP 500
    #def get_ranks(self, gamertag):
    #    url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/ranks" % gamertag
    #    return self._fetch_json(url)

    def get_campaign_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/servicerecord/campaign" % gamertag
        return self._fetch_json(url)

    def get_spartanops_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/servicerecord/spartanops" % gamertag
        return self._fetch_json(url)

    def get_wargame_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/servicerecord/wargames" % gamertag
        return self._fetch_json(url)

    def get_customgame_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-US/players/%s/h4/servicerecord/custom" % gamertag
        return self._fetch_json(url)

    def get_spartan_image(self, gamertag, pose, params=None):
        url = "https://spartans.svc.halowaypoint.com/players/%s/h4/spartans/%s" % (gamertag, pose)
        return self._fetch_png(url, params)

    def _fetch_json(self, url, params=None):
        r = requests.get(url,
                         headers={
                             'user-agent': 'PyHalo/0.1 (%s)' % self.waypoint_token.live_username,
                             'accept': 'application/json',
                             'Accept-Encoding': 'gzip,deflate',
                             'X-343-Authorization-Spartan': self.waypoint_token.spartan_token
                         },
                         params=params,
                         verify=False
        )
        return r.json()

    def _fetch_png(self, url, params=None):
        r = requests.get(url,
                         headers={
                             'user-agent': 'PyHalo/0.1 (%s)' % self.waypoint_token.live_username,
                             'accept': 'image/png',
                             'Accept-Encoding': 'gzip,deflate',
                             'X-343-Authorization-Spartan': self.waypoint_token.spartan_token
                         },
                         params=params,
                         verify=False
        )
        return r.content
