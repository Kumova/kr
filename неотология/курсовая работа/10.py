import requests
from pprint import pprint
import time
from tqdm import tqdm
import yadisk
import json
import os
from datetime import datetime


for i in tqdm(range(5)):
      time.sleep(1)

#y = yadisk.YaDisk(token="AQAAAAA6dFGUAADLW5eadxA57knHvF5C86l7aAw")
#print(y.check_token())
#print(y.get_disk_info())


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
                'offset': 0,
                'count': 5,
                'photo_sizes': 0,
                'v': 5.131
        }


        filename=url.split('/')[-1]
        r = requests.get(url, params=params)
        pprint(r.json()['response']['items'])
        for i in r.json()['response']['items']:
            self.y = (i['likes']['count'])
            for j in r.json()['response']['items']:
               self.j = j


    def create_dict(self):
         dct = {self.y: self.j}
         with open('photos.json', 'w') as f:
#             for j in dct:
#                 content = '\n'.join(dct['content_file'])
 #                f.write(f"{dct['name_file']}\n{dct['likes']['count']}\n{'size'}\n")
              json.dump(dct, f, ensure_ascii=False, indent=2)
         with open('photos.json', encoding='UTF-8') as f:
             dct=json.load(f)
         pprint(dct)


class Yandex:
    y = yadisk.YaDisk(token="AQAAAAA6dFGUAADLW5eadxA57knHvF5C86l7aAw")
    print(y.check_token())
    print(y.get_disk_info())
#    y.mkdir("work")
#    replace=False
#    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    loadfile = 'C:\photos.json'
    savefile = 'https://disk.yandex.ru/client/disk/work'
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        requests.put(res['href'], files={'file': f})
        except KeyError:\
            print(res)




if __name__ == '__main__':
    vk = VK('a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd', 5.131)
    vk.get_photo()
    vk.create_dict()


