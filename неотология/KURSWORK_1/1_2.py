import requests
import yadisk_api
import json

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
        data=r.json()['response']['items']
        dict_1=[]
        for i in dict_1:
            dict = {}
            with open('photo.json', 'w') as outfile:
                dict['name'] = i['likes']['count']
                dict['sizes'] = i['sizes']
                dict_1.append(dict)
                dict_1 = sorted(dict_1, key=lambda dict_: dict['type'])
                json.dump(dict_1, outfile, sort_keys=True, indent=4)
                content = '\n'.join(dict['name'])
                outfile.write(f"{dict['name']}\n{dict['likes']['count']['sizes']}\n{content}\n")

class YaDisk:
    def __init__(self, token):
        self.token = token

    def post_photo(self, photos):
        token='AAw'
        headers={'Autorization': self.token}
        for dict_1 in enumerate(photos):
            params = {
                "path": f"C:\KURSWORK_1{dict_1['name']}",
                "overwrite": True,
                'url': dict_1['url']
            }

        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.post(url, headers=headers, params=params)
        print(response.json())

if __name__ == '__main__':
    vk = VK('a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd', 5.131)
    vk.get_photo()
    yadisk_api = YaDisk('86l7aAw')
    yadisk_api.post_photo('photos')


