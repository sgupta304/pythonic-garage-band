from pythonic_garage_band.members.musician import Musician


class Guitarist(Musician):

    def __init__(self, name, solo_song=None):
        super(Guitarist, self).__init__(name, "guitar", solo_song)

    def play_solo(self):
        return f"I'm the {self.__class__.__name__}, and I'm going to sing {self.solo_song}"

    def get_instrument(self):
        return f"I'm the {self.__class__.__name__}, and I play the {self.instrument}"
