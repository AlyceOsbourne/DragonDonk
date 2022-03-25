from enum import Enum, auto
from dataclasses import dataclass

class CreatureType(Enum):
    Aberration = auto()
    Beast = auto()
    Celestial = auto()
    Construct = auto()
    Dragon = auto()
    Elemental = auto()
    Fey = auto()
    Fiend = auto()
    Giant = auto()
    Humanoid = auto()
    Monstrosity = auto()
    Ooze = auto()
    Plant = auto()
    Undead = auto()

class Size(Enum):
    Tiny = auto()
    Small = auto()
    Medium = auto()
    Large = auto()
    Huge = auto()
    Gargantuan = auto()

class MovementType(Enum):
    Walking = auto()	
    Burrow = auto()	
    Climb = auto()	
    Fly = auto()	
    Swim = auto()


    
    


    

    

    


