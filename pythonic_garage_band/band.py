import weakref


class Band:
    _instances = set()

    def __init__(self, band_name):
        self.band_name = band_name
        self.__members = []
        self._instances.add(weakref.ref(self))

    def add_band_member(self, new_members):
        for new_member in new_members:
            self.__members.append(new_member)

    def play_solos(self):
        solos = ''
        for member in self.__members:
            solos += member.play_solo() + ', '
        return solos

    @classmethod
    def to_list(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead
        return cls._instances

    @staticmethod
    def create_from_data(data):
        pass

    def __str__(self):
        return f"We are {self.__class__.__name__}, and our name is {self.band_name}."

    def __repr__(self):
        return f"Band with {self.__class__.__name__} instance."
