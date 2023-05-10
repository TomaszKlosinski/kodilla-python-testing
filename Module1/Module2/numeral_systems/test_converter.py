import converter

def test_to_roman():
    assert converter.to_roman(0) == None
    assert converter.to_roman(1) == "I"
    assert converter.to_roman(3) == "III"
    assert converter.to_roman(5) == "V"
    assert converter.to_roman(9) == "IX"
    assert converter.to_roman(40) == "XL"
    assert converter.to_roman(1904) == "MCMIV"


def test_from_roman():
    assert converter.from_roman("I") == 1
    assert converter.from_roman("III") == 3
    assert converter.from_roman("V") == 5
    assert converter.from_roman("IX") == 9
    assert converter.from_roman("XL") == 40
    assert converter.from_roman("MCMIV") == 1904
