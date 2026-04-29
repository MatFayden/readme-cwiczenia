def szyfruj_vigenere(tekst, klucz):
    """Szyfruje tekst za pomocą szyfru Vigenère'a.

    Args:
        tekst (str): Tekst do zaszyfrowania.
        klucz (str): Słowo kluczowe.

    Returns:
        str: Zaszyfrowany tekst (wielkie litery).

    Raises:
        ValueError: Jeśli klucz jest pusty.
    """
    if not klucz:
        raise ValueError("Klucz nie może być pusty")
        
    wynik = ""
    key_index = 0
    tekst = tekst.upper()
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():
            wartosc_litery = ord(litera) - ord('A')
            wartosc_klucza = ord(klucz[key_index % len(klucz)]) - ord('A')

            zaszyfrowana_wartosc = (wartosc_litery + wartosc_klucza) % 26
            wynik += chr(zaszyfrowana_wartosc + ord('A'))
            key_index += 1
        else:
            wynik += litera
    return wynik


def deszyfruj_vigenere(zaszyfrowany_tekst, klucz):
    """Deszyfruje tekst zaszyfrowany szyfrem Vigenère'a.

    Args:
        zaszyfrowany_tekst (str): Tekst do odszyfrowania.
        klucz (str): Słowo kluczowe użyte do szyfrowania.

    Returns:
        str: Odszyfrowany tekst (wielkie litery).

    Raises:
        ValueError: Jeśli klucz jest pusty.
    """
    if not klucz:
        raise ValueError("Klucz nie może być pusty")
        
    wynik = ""
    key_index = 0
    zaszyfrowany_tekst = zaszyfrowany_tekst.upper()
    klucz = klucz.upper()

    for litera in zaszyfrowany_tekst:
        if litera.isalpha():
            wartosc_litery = ord(litera) - ord('A')
            wartosc_klucza = ord(klucz[key_index % len(klucz)]) - ord('A')

            odszyfrowana_wartosc = (wartosc_litery - wartosc_klucza) % 26
            wynik += chr(odszyfrowana_wartosc + ord('A'))
            key_index += 1
        else:
            wynik += litera
    return wynik


if __name__ == "__main__":
    oryginalny_tekst = "PROGRAMOWANIE JEST SUPER!"
    klucz = "abc"
    zaszyfrowany = szyfruj_vigenere(oryginalny_tekst, klucz)
    odszyfrowany = deszyfruj_vigenere(zaszyfrowany, klucz)
    print(f"Zaszyfrowany: {zaszyfrowany}")
    print(f"Odszyfrowany: {odszyfrowany}")
