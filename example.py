__author__ = 'Damon Pollard (@DamonLPollard)'

import pyhalo.api
import pyhalo.authentication


WLID_USERNAME = ''
WLID_PASSWORD = ''
GAMERTAG = 'Furiousn00b'
GAMERTAGS = ['Furiousn00b', 'SLOPPYPOCKET420', 'elgnairT', 'OAKSImp']
GAME_ID = 'a0476654a118e570'


#Authentication
waypoint_token = pyhalo.authentication.HaloFour(WLID_USERNAME, WLID_PASSWORD).get_new_token()
api = pyhalo.api.HaloFour(waypoint_token)

# Get API version.
api_version = api.get_api_version()

# Get API services.
api_services = api.get_api_services()

# Get a gamers Halo 4 Achievements.
user_achievements = api.get_user_achievements({'requesteeGamertag': GAMERTAG, 'titleId': '1297287449'})
''' requesteeGamertag = GAMERTAG
    titleId = 1297287449
'''

# Get Halo Four Playlist details.
playlists = api.get_playlists()

# Get active Halo Four challenges.
global_challenges = api.get_global_challenges()

# Get *authenticated* gamers challenge progess.
player_challenges = api.get_player_challenges()

# Get Halo Four metadata (large)
metadata = api.get_game_metadata({'type': 'armor,player-upgrades,poses'})
''' type = [achievements, armor, challenges, commendations, damage-types, difficulty, emblems, enemies, factions,
            game-base-variants, game-modes, maps, medals, narrative-flags, player-upgrades, playlists, poses,
            promotion-types, rankawards, ranks, skulls, spartanops, specializations, team-appearance]
'''

# Get a gamers Player Card.
playercard = api.get_playercard(GAMERTAG)

# Get multiple gamers Player Cards.
playercards = api.get_multiple_playercards({'gamertags': ",".join(GAMERTAGS)})
''' gamertags = [gamertag_one, gamertag_two, ...]
'''

# Get a gamers Service Record.
service_record = api.get_service_record(GAMERTAG)

#Get a gamertags game history. Includes games from WarGames, Custom, SpartanOps and Campaign.
game_history = api.get_game_history(GAMERTAG, {'count': 10, 'startat': 0})
''' gamemodeid = Metadata -> GameModesMetadata -> GameModes -> GameModeMetadata
    mapid = Metadata -> MapsMetadata -> Maps -> MapMetadata
    count = 1-100
    startat = 0-32767
    chapterid = Metadata -> SpartanOpsMetadata -> Seasons -> SeasonMetadata -> Episodes -> EpisodeMetadata
'''

# Get a games details.
game_details = api.get_game_details(GAME_ID)

# Get a gamertags commendation progress.
commendations = api.get_commendations(GAMERTAG)

# Get a gamers ranks (?) HTTP 500
# ranks = api.get_ranks(GAMERTAG)

# Get a gamers Campaign details.
campaign_details = api.get_campaign_details(GAMERTAG)

# Get a gamers SpartanOps details.
spartanops_details = api.get_spartanops_details(GAMERTAG)

# Get a gamers WarGames details.
wargame_details = api.get_wargame_details(GAMERTAG)

# Get a gamers Custom Game details.
customgame_details = api.get_customgame_details(GAMERTAG)

# Get a gamers Spartan Image.
spartan_image = api.get_spartan_image(GAMERTAG, 'fullbody', {'target': 'large'})
''' pose = [fullbody, posed]
    target = [small, medium, large]
'''
