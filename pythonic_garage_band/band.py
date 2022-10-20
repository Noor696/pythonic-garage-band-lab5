from abc import abstractmethod, ABC
from unicodedata import name

# ___________Band instance_______________#

class Band:

    instances = []

    def __init__(self, name, members) -> None:
        self.name=name
        self.members=members
        Band.instances.append(self)

    def play_solos(self):
        solos =[]
        for i in self.members:
            solos.append(i.play_solo())
        return solos

    def __str__(self):
        return f'{self.name} band'

    def __repr__(self):
        return f"Name = {self.name}"

    @classmethod
    def to_list(cls) :
        return cls.instances   

# ___________class Musician (base class)_______________#


class Musician(ABC):
    def __init__(self, name) -> None:
        self.name = name


    def __str__(self):
            return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
            return f"{self.__class__.__name__} instance. Name = {self.name}"
    
    def play_solo(self):
            return self.play_solos()

# ___________class Guitaris (Musician Subclass)_______________#

class Guitarist(Musician):

    def __init__(self, name) -> None:
        super().__init__(name)

    
    def play_solo(self):
        return "face melting guitar solo"

    @staticmethod
    def get_instrument():
        return "guitar"

# ___________class Bassist (Musician Subclass)_______________#

class Bassist(Musician):
    def __init__(self, name) -> None:
        super().__init__(name)

    
    def play_solo(self):
        return "bom bom buh bom"

    @staticmethod
    def get_instrument():
        return "bass"

# ___________class Drummer (Musician Subclass)_______________#


class Drummer(Musician):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    
    def play_solo(self):
        return "rattle boom crash"

    @staticmethod
    def get_instrument():
        return "drums"


# ____________________________
test = Band("noor", [Guitarist("first person"), Bassist("second person"), Drummer("third person")])

print (test.play_solos())  #output ['face melting guitar solo', 'bom bom buh bom', 'rattle boom crash']