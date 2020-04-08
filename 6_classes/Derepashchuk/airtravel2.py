"""Model for Aircraft flights"""


__all__ = ['Flight', 'Aircraft']


class Flight:
    """A flight with a particular passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number {}".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def route_number(self):
        return self._number[2:]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21B'.
            passenger: The passenger name.

        Raises:
            ValueError: if the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))

        self._seating[row][letter] = passenger

    def free_seat(self, seat, passenger):
        """Free seat from a passenger.


        Args:
            seat: A seat designator such as '12C' or '21B'.
            passenger: The passenger name.

        Raises:
            ValueError: if the seat is free or allocated not for this passenger.
        """

        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        if self._seating[row][letter] is None:
            raise ValueError("Seat {} is already free".format(seat))

        if self._seating[row][letter] == passenger:
            self._seating[row][letter] = None
        else:
            raise ValueError(f"Seat {seat} is occupied not by {passenger}")

    def move_seat(self, old_seat, new_seat):
        """Move passenger from one seat to another.

        Args:
            old_seat: A seat designator such as '12C' or '21B'.
            new_seat: A seat designator we move the passenger.

        Raises:
            ValueError: if the old_seat is free or new_seat is occupied.
        """
        pass


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seat_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seat_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

    def all_info(self):
        return self._registration, self._model, self._num_rows


f = Flight("QR277", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seat_per_row=6))
f.allocate_seat('5B', 'Petro')
a, b, c = f._aircraft.all_info()
print(a)
print(b)
print(c)