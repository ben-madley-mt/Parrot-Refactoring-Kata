class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
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
    pass

class AfricanParrot(Parrot):
    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self):
        return "Sqaark!"

    def _load_factor(self):
        return 9.0


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

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])


class ParrotType:
    EUROPEAN = EuropeanParrot
    AFRICAN = AfricanParrot
    NORWEGIAN_BLUE = NorwegianBlueParrot

    @staticmethod
    def make(type_of_parrot, number_of_coconuts, voltage, nailed):
        return type_of_parrot(type_of_parrot, number_of_coconuts, voltage, nailed)