"""Model of world creatures"""


class Animal:
    """Animal class description"""

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def is_heterotrophic(self):
        return True

    def is_animal(self):
        return True


class Mammal(Animal):
    """brain, milk, hair"""

    def has_brain(self):
        return True

    def drink_milk(self):
        return True

    def has_hair(self):
        return True


class Wolf(Mammal):

    def beat(self):
        print("You are bitten now!")

    def run(self):
        print("I run 30 km/h!")


class Human(Mammal):

    def speak(self):
        print("Hello, I am a human.")

    def sing(self):
        print("Tralala!")

    def run(self):
        print("I run 10 km/h!")


class Werewolf(Wolf, Human):

    def run(self):
        print()
        super(Werewolf, self).run()
        print("I don't like run, I like eat!")

    def full_moon(self):
        print("Woooooooooo!")

class Bird:
    # wings, eggs
    pass


class Fish:
    # gill
    pass


class Reptile:
    # poikilotherm
    pass


class Amphibian:
    # metamorphosis
    pass
