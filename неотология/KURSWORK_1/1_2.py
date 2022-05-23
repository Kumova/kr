import requests
from pprint import pprint
import time
from tqdm import tqdm
import yadisk
import json
import os
import sys
import urllib
import math
from datetime import datetime



numbers_photo=0

class VK:

    def __init__(self, token, v):
        self.token = token
        self.v = v


    def get_photo(self):

        token = 'a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd'
        url = 'https://api.vk.com/method/photos.get'

        params = {
                'owner_id':   552934290,
                'access_token': token,
                'album_id': 'profile',
                'extended': 1,
                'offset': 1,
                'count': 1,
                'photo_sizes': 1,
                'v': 5.131
        }

        r = requests.get(url, params=params)
        data=r.json()
        dict_data=[]
        for item in data.items():
            with open('photo.json', 'w') as outfile:
                json.dump(data, outfile, sort_keys=True, indent=4)
            #            print(item)
        my_list = r.json()['response']['items']
 #       result_list = []
        for i in dict_data:
            temp_dict = {}
            with open('photo.json', 'w', encoding='utf-8') as file:
                temp_dict['name_file'] = i['likes']['count']
                temp_dict['size'] = i['size']
                dict_data.append(temp_dict)
        dict_data = sorted(dict_data, key=lambda temp_dict: temp_dict['type'])
        with open('new.json', "w", encoding='utf-8') as fh:
            for dict_ in dict_data:
                content = '\n'.join(dict_['name_file'])
                fh.write(f"{dict_['name_file']}\n{dict_['likes']['count']['type']}\n{content}\n")

class YaDisk:
    def __init__(self, token):
        self.token = token

    def post_photo(self):
        y = yadisk.YaDisk(token="AQAAAAA6dFGUAADLW5eadxA57knHvF5C86l7aAw")
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.post(url, params='result_list')
        print(response.json())

if __name__ == '__main__':
    vk = VK('a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd', 5.131)
    vk.get_photo()
    YaDisk = YaDisk('AQAAAAA6dFGUAADLW5eadxA57knHvF5C86l7aAw')
    YaDisk.post_photo()

