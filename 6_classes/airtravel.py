"""Model for Aircraft flights"""


class Flight:

    def __init__(self, number):
        self._number = number

    def number(self):
        return self._number


class Passenger:

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

