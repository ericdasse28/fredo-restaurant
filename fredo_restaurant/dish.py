from enum import Enum


class PastaType(Enum):
    FUSILLI = "fusilli"
    PENNE = "penne"
    SPAGHETTI = "spaghetti"


class Salsa(Enum):
    BOLOGNAISE = "bolognaise"
    CARBONARA = "carbonara"
    CHILI = "chili"


class Topping(Enum):
    BEEF = "beef"
    CHICKEN = "chicken"
    MUSHROOMS = "mushrooms"
