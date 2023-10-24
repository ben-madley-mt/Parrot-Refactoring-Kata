from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3

def european(number_of_coconuts, voltage, nailed):
    return EuropeanParrot(ParrotType.EUROPEAN, number_of_coconuts, voltage, nailed)
def african(number_of_coconuts, voltage, nailed):
    return AfricanParrot(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)
def norwegian_blue(number_of_coconuts, voltage, nailed):
    return NorwegianBlueParrot(ParrotType.NORWEGIAN_BLUE, number_of_coconuts, voltage, nailed)

class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def get_subtype(self):
        if self._type == ParrotType.EUROPEAN:
            return european(self._number_of_coconuts, self._voltage, self._nailed)
        if self._type == ParrotType.AFRICAN:
            return african(self._number_of_coconuts, self._voltage, self._nailed)
        if self._type == ParrotType.NORWEGIAN_BLUE:
            return norwegian_blue(self._number_of_coconuts, self._voltage, self._nailed)

        raise ValueError("should be unreachable")

    def speed(self):
        return self.get_subtype().speed()

    def cry(self):
        return self.get_subtype().cry()


    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0


class EuropeanParrot(Parrot):
    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self):
        return "Sqaark!"


class NorwegianBlueParrot(Parrot):
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
