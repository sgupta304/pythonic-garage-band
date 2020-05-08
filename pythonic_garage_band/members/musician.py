from abc import ABC, abstractmethod


class Musician(ABC):
    def __init__(self, musician_name, instrument, solo_song):
        self.musician_name = musician_name
        self.solo_song = solo_song
        self.instrument = instrument

    @abstractmethod
    def play_solo(self):
        return self.solo_song

    @abstractmethod
    def get_instrument(self):
        return self.instrument

    def __str__(self):
        return f"I am a(an) {self.__class__.__name__}, and my name is {self.musician_name}."

    def __repr__(self):
        return f"Musician with {self.__class__.__name__} instance."
