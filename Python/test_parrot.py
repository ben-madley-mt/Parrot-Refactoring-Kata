from parrot import ParrotType


def test_speedOfEuropeanParrot():
    parrot = ParrotType.make(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_cryOfEuropeanParrot():
    parrot = ParrotType.make(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.cry() == "Sqoork!"


def test_speedOfAfricanParrot_With_One_Coconut():
    parrot = ParrotType.make(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.speed() == 3.0


def test_cryOfAfricanParrot():
    parrot = ParrotType.make(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.cry() == "Sqaark!"


def test_speedOfAfricanParrot_With_Two_Coconuts():
    parrot = ParrotType.make(ParrotType.AFRICAN, 2, 0, False)
    assert parrot.speed() == 0.0


def test_speedOfAfricanParrot_With_No_Coconuts():
    parrot = ParrotType.make(ParrotType.AFRICAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_speedNorwegianBlueParrot_nailed():
    parrot = ParrotType.make(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
    assert parrot.speed() == 0.0


def test_speedNorwegianBlueParrot_not_nailed():
    parrot = ParrotType.make(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
    assert parrot.speed() == 18.0


def test_speedNorwegianBlueParrot_not_nailed_high_voltage():
    parrot = ParrotType.make(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.speed() == 24.0

def test_cryNorwegianBlueParrot_high_voltage():
    parrot = ParrotType.make(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.cry() == "Bzzzzzz"

def test_cryNorwegianBlueParrot_no_voltage():
    parrot = ParrotType.make(ParrotType.NORWEGIAN_BLUE, 0, 0, False)
    assert parrot.cry() == "..."
