"""
config values needed to initialize each of the different services. We now need an interface
that will use these values to create concrete classes.
"""
from python.designpatterns.factoryPattern.musicservices import music

config = {
    'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
    'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
    'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
    'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET',
    'local_music_location': '/usr/data/music'
}

pandora = music.services.get('PANDORA', **config)
pandora.test_connection()

spotify = music.services.get('SPOTIFY', **config)
spotify.test_connection()

local = music.services.get('LOCAL', **config)
local.test_connection()



