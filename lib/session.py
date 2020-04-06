import json
from datetime import datetime
import base64

import utils.dict_utils

import utils.services
import utils.league
import utils.dragon

class Session:
    def __init__(self, patch):
        self.changePatch(patch)

    def changePatch(self, patch):
        self._patch = patch
        self._champions = utils.dragon.get_champions_list(self._patch)
        self._champions_id_dict = utils.dragon.key_as_key(self._champions)
        self._items = utils.dragon.get_items_list(self._patch)
        self._items_id_dict = self._items["data"]
        self._summoners = utils.dragon.get_summoners_list(self._patch)
        self._summoners_id_dict = utils.dragon.key_as_key(self._summoners)

    def patch(self):
        self._patch
    def champions(self):
        self._champions
    def champions_id_dict(self):
        self._champions_id_dict
    def items(self):
        self._items
    def items_id_dict(self):
        self._items_id_dict
    def summoners(self):
        self._summoners
    def summoners_id_dict(self):
        self._summoners_id_dict


    # Display functions
    def image_from_item(self, item, height = '30px', width = '30px'):
        if utils.dict_utils.access(self._items_id_dict, [f"{item}"]):
            return utils.html.Image(utils.dragon.item_img_url(item, self._patch), height, width)._repr_html_()
        return "<div></div>"

    def image_from_champion(self, champion, height = '50px', width = '50px'):
        if utils.dict_utils.access(self._champions_id_dict, [f"{champion}"]):
            return utils.html.Image(utils.dragon.champion_img_url(self._champions_id_dict[champion], self._patch), height, width)._repr_html_()
        return "<div></div>"
