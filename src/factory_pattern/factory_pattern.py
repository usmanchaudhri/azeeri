"""
Build factory pattern which supports multiple languages
"""

class FrenchLocalizer:

    """ it simply returns the french version """
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}

    def localize(self, message):
        return self.translations.get(message)

class SpanishLocalizer:

    """ it simply returns the spanish version """
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, message):
        return self.translations.get(message)

class EnglishLocalizer:

    """ it simply returns the spanish version """
    def __init__(self):
        self.translations = {"car": "car", "bike": "bike", "cycle": "cycle"}

    def localize(self, message):
        return self.translations.get(message)

def Factory(language ="English"):
    """ Factory Method """
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer
    }
    return localizers[language]()

if __name__== "__main__":
    f = Factory("French")
    s = Factory("Spanish")
    e = Factory("English")

    message = ["car", "bike", "cycle"]
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))






