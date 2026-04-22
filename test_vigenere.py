import pytest
from vigenere import szyfruj_vigenere, deszyfruj_vigenere

@pytest.fixture
def default_key():
    return "SECRET"

@pytest.mark.basic
def test_vigenere_with_fixture(default_key):
    tekst = "HELLO"
    zaszyfrowany = szyfruj_vigenere(tekst, default_key)
    odszyfrowany = deszyfruj_vigenere(zaszyfrowany, default_key)
    assert odszyfrowany == tekst

@pytest.mark.basic
@pytest.mark.parametrize("tekst, klucz, expected", [
    ("AAA", "A", "AAA"),
    ("ABCDE", "AB", "ACCEE"),
    ("Z", "B", "A"),
    ("HELLO WORLD!", "KEY", "RIJVS UYVJN!"),], ids=["zero_shift", "loop_key", "wrap_z", "special_chars"])
def test_vigenere_parametrized(tekst, klucz, expected):
    assert szyfruj_vigenere(tekst, klucz) == expected

@pytest.mark.exceptions
def test_vigenere_empty_key():
    with pytest.raises(ValueError):
        szyfruj_vigenere("ABC", "")

@pytest.mark.extended
def test_vigenere_long_text(default_key):
    tekst = "TO JEST BARDZO DLUGI TEKST DO TESTOWANIA SZYFRU VIGENEREA"
    zaszyfrowany = szyfruj_vigenere(tekst, default_key)
    assert deszyfruj_vigenere(szyfruj_vigenere(tekst, default_key), default_key) == tekst.upper()
