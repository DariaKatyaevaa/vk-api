import requests
from urllib.parse import urlencode


class API:
    def __init__(self, token, version='5.103'):
        self.token = token
        self.version = version

    @staticmethod
    def get_url(method, **kwargs):
        return 'https://api.vk.com/method/{}?{}'.format(method, urlencode(kwargs))

    def request(self, method, **kwargs):
        kwargs.setdefault('v', self.version)
        kwargs.setdefault('access_token', self.token)
        return requests.get(self.get_url(method, **kwargs)).json()

    def get_friends(self, user_id):
        response = self.request('friends.get', user_id=user_id, order='hints')['response']['items']
        print("Список друзей:")
        for friend in response:
            self.get_user_name(friend)

    def get_albums(self, user_id):
        response = self.request('photos.getAlbums', owner_id=user_id)['response']['items']
        print('Список альбомов:')
        for items in response:
            print(items['title'])

    def get_user_name(self, user_id):
        user = self.request('users.get', user_ids=user_id)['response'][0]
        print(user["first_name"] + ' ' + user["last_name"])
