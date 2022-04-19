import requests
from pprint import pprint
from tqdm import tqdm
import yadisk
from urllib.request import urlretrieve
import vkapi, os, time, math



for i in tqdm(range(5)):
      time.sleep(1)




class VK:

    def __init__(self, token, v):
        self.token = token
        self.v = v


    def get_photo(self):


        token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
        url = 'https://api.vk.com/method/photos.get'

        params = {
                'owner_id':  315660313,
                'access_token': token,
                'album_id': 'profile',
                'extended': 1,
                'offset': 0,
                'photo_count': 50,
                'photo_sizes': 0, 
                'v': 5.131
        }


        filename=url.split('/')[-1]
        r = requests.get(url, params=params).content
        pprint(r.json()['response']['items'])
        for i in r.json()['response']['items']:
            self.y = (i['likes']['count'])
            for j in r.json()['response']['items']:
               self.j = j

        if r.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(r.content)






    def create_dict(self):
         dct = {self.y: self.j}
#         with open('dct.txt', 'w') as outfile:
#             json.dump(dct, outfile)
         pprint(dct)


class Yandex:
     y = yadisk.YaDisk(token="[[[[[[]]]]]]")
     print(y.check_token())
     print(y.get_disk_info())
     y.mkdir("kurs_work")
     with open("photos.get", "rb") as f:
        y.upload(f, "photos.get")



if __name__ == '__main__':
    vk = VK('958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008', 5.131)
    vk.get_photo()
    vk.create_dict()

