"""
The song object has a serialize method which serializes the song object, it takes as a method parameter
the serializer - format which the song object will be serialized to - and the serializer than converts
the song object into the respective serialization format.
This way we can pass-in any serialization method to the serialize() and it will perform the specific
serialization
"""

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)



