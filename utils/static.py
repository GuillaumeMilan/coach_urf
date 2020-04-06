import utils.services
import json

### STATIC LEAGUE OF LEGENDS API FUNCTIONS ###
def get_queues():
    r = utils.services.fetch_statics(f"/docs/lol/queues.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_maps():
    r = utils.services.fetch_statics(f"/docs/lol/maps.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_modes():
    r = utils.services.fetch_statics(f"/docs/lol/gameModes.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_types():
    r = utils.services.fetch_statics(f"/docs/lol/gameTypes.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

### TO DICTIONARY ###
def to_dict(l, key):
    return {obj[key]: obj for obj in l}
