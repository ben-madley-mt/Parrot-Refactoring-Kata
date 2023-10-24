from enum import Enum


class Parrot:

    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"

    def _base_speed(self):
        return 12.0


class EuropeanParrot(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self):
        return "Sqaark!"

    def _load_factor(self):
        return 9.0


class NorwegianBlueParrot(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        if self._nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        if self._voltage > 0:
            return "Bzzzzzz"
        else:
            return "..."

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3

    @staticmethod
    def make(type_of_parrot, number_of_coconuts, voltage, nailed):
        if type_of_parrot == ParrotType.EUROPEAN:
            return EuropeanParrot(number_of_coconuts, voltage, nailed)
        if type_of_parrot == ParrotType.AFRICAN:
            return AfricanParrot(number_of_coconuts, voltage, nailed)
        if type_of_parrot == ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(number_of_coconuts, voltage, nailed)

        raise ValueError("should be unreachable")

