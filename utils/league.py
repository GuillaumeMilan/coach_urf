import utils.services
import json
### RIOT API FUNCTIONS
def get_user(user_name):
    r = utils.services.fetch_riot_API(f"/lol/summoner/v4/summoners/by-name/{user_name}")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_rotation():
    r = utils.services.fetch_riot_API(f"/lol/platform/v3/champion-rotations")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_masteries(user_id):
    r = utils.services.fetch_riot_API(f"/lol/champion-mastery/v4/champion-masteries/by-summoner/{user_id}")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_history(account_id):
    r = utils.services.fetch_riot_API(f"/lol/match/v4/matchlists/by-account/{account_id}")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_match(gameId):
    r = utils.services.fetch_riot_API(f"/lol/match/v4/matches/{gameId}")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_match_timeline(gameId):
    r = utils.services.fetch_riot_API(f"/lol/match/v4/timelines/by-match/{gameId}")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_all_the_league_entries(queue,tier,division):
    r = utils.services.fetch_riot_API(f"/lol/league/v4/entries/{queue}/{tier}/{division}")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_league(leagueId):
    r = utils.services.fetch_riot_API(f"/lol/league/v4/leagues/{leagueId}")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None
