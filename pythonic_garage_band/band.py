from abc import abstractmethod, ABC

class Band:

    instances = []
    def __init__(self, name, members) -> None:
        self.name=name
        self.members=members
        Band.instances.append(self)

    def play_solos():
        pass


class Musician(ABC):
    def __init__(self, name) -> None:
        self.name = name

class Guitarist(Musician):
    def __init__(self) -> None:
        super().__init__()


class Bassist(Musician):
    def __init__(self) -> None:
        super().__init__()


class Drummer(Musician):
    def __init__(self) -> None:
        super().__init__()