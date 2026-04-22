import pytest
from cezar import cezar, lamanie_cezara

@pytest.mark.basic
@pytest.mark.parametrize("napis, klucz, expected", [
    ("abc", 1, "BCD"),
    ("abc", 2, "CDE"),
    ("XYZ", 3, "ABC"),
    ("Hello World!", 5, "MJQQT BTWQI!"),
    ("", 10, ""),
], ids=["shift_1", "shift_2", "zawijanie", "znaki_specjalne", "pusty"])
def test_cezar_parametrized(napis, klucz, expected):
    assert cezar(napis, klucz) == expected

@pytest.mark.extended
def test_cezar_decrypt():
    original = "TESTOWANIE"
    encrypted = cezar(original, 7)
    decrypted = cezar(encrypted, -7)
    assert decrypted == original

@pytest.mark.extended
def test_cezar_lamanie():
    oryginal = "LOKOMOTYWA STOI NA STACJI"
    zaszyfrowane = cezar(oryginal, 10)
    wynik = lamanie_cezara(zaszyfrowane)
    assert oryginal == wynik

@pytest.mark.exceptions
def test_cezar_wrong_type():
    with pytest.raises(TypeError):
        cezar(123, 5)
