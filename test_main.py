import pytest
from main import generuj_klucz

@pytest.mark.basic
def test_generuj_klucz_cezar():
    klucz = generuj_klucz("cezar")
    assert isinstance(klucz, int)
    assert 1 <= klucz <= 25

@pytest.mark.basic
def test_generuj_klucz_vigenere():
    klucz = generuj_klucz("vigenere", 15)
    assert isinstance(klucz, str)
    assert len(klucz) == 15
    assert klucz.isupper()

@pytest.mark.exceptions
def test_generuj_klucz_invalid():
    with pytest.raises(ValueError):
        generuj_klucz("unknown")
