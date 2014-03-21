__author__ = 'Damon Pollard (@DamonLPollard)'

import requests


class HaloFour():
    def __init__(self, waypoint_token):
        self.waypoint_token = waypoint_token

    def get_global_challenges(self):
        url = "https://stats.svc.halowaypoint.com/en-us/h4/challenges"
        return self._fetch_json(url)

    def get_player_challenges(self):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/challenges" % self.waypoint_token.gamertag
        return self._fetch_json(url)

    def get_game_metadata(self):
        url = "https://stats.svc.halowaypoint.com/en-us/h4/metadata"
        return self._fetch_json(url)

    def get_playercard(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/playercard" % gamertag
        return self._fetch_json(url)

    def get_multiple_playercards(self, gamertags):
        url = "https://stats.svc.halowaypoint.com/en-us/h4/playercards?gamertags=%s" % ",".join(gamertags)
        return self._fetch_json(url)

    def get_service_record(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/servicerecord" % gamertag
        return self._fetch_json(url)

    def get_game_history(self, gamertag, gamemodeid, count, startindex):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/matches?gamemodeid=%dcount=%d&startat=%d" \
              % (gamertag, gamemodeid, count, startindex)
        return self._fetch_json(url)

    def get_game_details(self, game_id):
        url = "https://stats.svc.halowaypoint.com/en-us/h4/matches/%s" % game_id
        return self._fetch_json(url)

    def get_commendations(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/commendations" % gamertag
        return self._fetch_json(url)

    def get_campaign_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/servicerecord/campaign" % gamertag
        return self._fetch_json(url)

    def get_spartanops_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/servicerecord/spartanops" % gamertag
        return self._fetch_json(url)

    def get_wargame_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/servicerecord/wargames" % gamertag
        return self._fetch_json(url)

    def get_customgame_details(self, gamertag):
        url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/servicerecord/custom" % gamertag
        return self._fetch_json(url)

    def get_playlists(self):
        url = "https://presence.svc.halowaypoint.com/en-us/h4/playlists"
        return self._fetch_json(url)

    #def get_ranks(self, gamertag):
    #    url = "https://stats.svc.halowaypoint.com/en-us/players/%s/h4/ranks" % (gamertag)
    #    return self.fetch_json(url)

    #def get_user_achievements(self, gamertag):
    #    url = "https://haloplayer.svc.halowaypoint.com/HaloPlayer/GetOtherUserAchievements" \
    #          "?requesteeGamertag=%s&titleId=1297287449" % gamertag
    #    return self.fetch_json(url)

    #def get_spartan_image(self, gamertag, pose, size):
    #    url = "https://spartans.svc.halowaypoint.com/players/%s/h4/spartans/%s?target=%s" % (gamertag, pose, size)
    #    return self.fetch(url)

    def _fetch_json(self, url):
        r = requests.get(url,
                         headers={
                             'user-agent': 'PyHalo/0.1 (gamertag: %s)' % self.waypoint_token.gamertag,
                             'accept': 'application/json',
                             'Accept-Encoding': 'gzip,deflate',
                             'X-343-Authorization-Spartan': self.waypoint_token.spartan_token
                         },
                         verify=False,
                         timeout=30)

        return r.json
