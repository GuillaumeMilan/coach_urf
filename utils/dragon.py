import utils.services
import json

### DRAGONS LEAGUE OF LEGENDS API FUNCTIONS ###
def get_patch():
    r = utils.services.fetch_dragons(f"/api/versions.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_current_patch():
    return get_patch()[0]

def get_champions_list(patch):
    r = utils.services.fetch_dragons(f"/cdn/{patch}/data/en_US/champion.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_items_list(patch):
    r = utils.services.fetch_dragons(f"/cdn/{patch}/data/en_US/item.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None

def get_summoners_list(patch):
    r = utils.services.fetch_dragons(f"/cdn/{patch}/data/en_US/summoner.json")
    if r.status >= 200 and r.status < 400:
        return json.loads(r.data)
    else:
        print(f"STATUS: {r.status}")
        return None


### DRAGON IMAGES API ###
def get_profil_icon_img_url(iconid, patch):
    return utils.services.url_dragons(f"/cdn/{patch}/img/profileicon/{iconid}.png")
def get_profil_icon_img(iconid,patch):
    img = utils.services.fetch_dragons(f"/cdn/{patch}/img/profileicon/{iconid}.png")
    return img

def champion_img_url(champion, patch):
    return utils.services.url_dragons(f"/cdn/{patch}/img/champion/{champion}.png")
def champion_img(champion, patch):
    img = utils.services.fetch_dragons(f"/cdn/{patch}/img/champion/{champion}.png")
    return img

def item_img_url(item, patch):
    return utils.services.url_dragons(f"/cdn/{patch}/img/item/{item}.png")
def item_img(item, patch):
    img = utils.services.fetch_dragons(f"/cdn/{patch}/img/item/{item}.png")
    return img

### DRAGONS ACCESS UTILS ###
def key_as_key(obj):
    return {body["key"] : name for name,body in obj["data"].items()}
