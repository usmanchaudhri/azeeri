"""

"""
class SpotifyService:
    def __init__(self, access_code):
        self._access_code = access_code

    def test_connection(self):
        print(f'Accessing spotify with {self._access_code}')

class SpotifyServiceBuilder:
    def __init__(self):
        self._instance: SpotifyService = None

    def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
        """
        create and initialize the concrete SpotifyService
        """
        if not self._instance:
            access_code = self.authorize(spotify_client_key, spotify_client_secret)
            self._instance = SpotifyService(access_code)
        return self._instance

    def authorize(self, key, secret):
        return 'SPOTIFY_ACCESS_CODE'


class PandoraService:
    def __init__(self, consumer_key, consumer_secret):
        self._key = consumer_key
        self._secret = consumer_secret

    def test_connection(self):
        print(f'Accessing Pandora with {self._key} and {self._secret}')

"""
The PandoraServiceBuilder implements the same interface, but it uses different parameters
 and processes to create and initialize the PandoraService. It also keeps the service 
 instance around, so the authorization only happens once.
"""
class PandoraServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, pandora_client_key, pandora_client_secret, **ignored):
        if not self._instance:
            consumer_key, consumer_secret = self.authorize(pandora_client_key, pandora_client_secret)
            self._instance = PandoraService(consumer_key, consumer_secret)
        return self._instance

    def authorize(self, key, secret):
        return 'PANDORE_CONSUMER_KEY', 'PANDORA_CONSUMER_SECRET'

"""
"""
class LocalService:
    def __init__(self, location):
        self._location = location

    def test_connection(self):
        print(f'Accessing Local music at {self._location}')

def create_local_music_service(local_music_location, **ignored):
    return LocalService(local_music_location)

from designpatterns.FactoryPattern.musicservices import object_factory

class MusicServiceProvider(object_factory.ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)

"""
You derive MusicServiceProvider from ObjectFactory and expose a new method .get(service_id, **kwargs).

This method invokes the generic .create(key, **kwargs), so the behavior remains the same, 
but the code reads better in the context of our application. You also renamed the previous 
factory variable to services and initialized it as a MusicServiceProvider.
"""
services = MusicServiceProvider()
services.register_builder('SPOTIFY', SpotifyServiceBuilder())
services.register_builder('PANDORA', PandoraServiceBuilder())
services.register_builder('LOCAL', create_local_music_service)


















