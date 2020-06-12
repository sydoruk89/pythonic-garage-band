class Musician:
    """
    Super class to all musicians. It has the next methods:
    __init__ - creates role and instrument attributes and append it to the list.
    __str__ - return a string with an object instance. 
    __repr__ - return a string readable for the Python interpreter. 
    play_solo - return a string indicating which musician plays solo.
    get_instrument - returns a string with instrument.
    """

    members = []

    def __init__(self, role, instrument):
        self.role = role
        self.instrument = instrument
        self.__class__.members.append(self)

    def __str__(self):
        return f'I am a {self.role}'

    def __repr__(self):
        return self.role
    
    def play_solo(self):
        return f'{self.role} is playing solo on the {self.instrument}'
    
    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    """Subclass that creates a new guitarist  and inherits properties from
    the Musician  super class"""

    pass


class Bassist(Musician):
    """Subclass that creates a new bassist and inherits properties from
    the Musician super class"""

    pass


class Drummer(Musician):
    """Subclass that creates a new drummer and inherits properties from
    the Musician super class"""

    pass


class Band:

    """
    This Class creates a Band instance and has the next class methods:
    __init__, __str__, __repr__, play_solos, to_list.
    """

    new_band = []

    def __init__(self, name, members=[]):
        """
        Creates name of the band and its members, and append new object instance to the list new_band
        """
        self.name = name
        self.members = members
        self.__class__.new_band.append(self)

    def play_solos(self):
        """
        Method that asks each member musician to play a solo, in the order they were added to band.
        """

        solo = ''
        for mus in self.members:
            solo += f'{mus}\n'
        return solo

    def __str__(self):
        """return string with the the object instance"""

        return f'We are the {self.name}'

    def __repr__(self):
        """return string with the object instance"""

        return ('The band name is ' + self.name)

    @classmethod
    def to_list(cls):
        """returns a list of previously created Band instances"""

        return cls.new_band


guitarist_1 = Guitarist('guitarist', 'guitar')
bassist_1 = Bassist('bassist', 'bass')
drummer_1 = Drummer('drummer', 'drumm')
print(guitarist_1.play_solo())

band_1 = Band('Wild dogs', Musician.members)
