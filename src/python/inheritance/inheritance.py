
class InvalidStreamException(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidStreamException("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidStreamException("Stream is already closed")
        self.opened = False