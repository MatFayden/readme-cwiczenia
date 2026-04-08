def szyfruj_vigenere(tekst, klucz):
    wynik = ""
    key_index = 0

    tekst = tekst.upper()
    klucz = klucz.upper()

    for litera in tekst:
        if 'A' <= litera <= 'Z':
            wartosc_litery = ord(litera) - ord('A')
            wartosc_klucza = ord(klucz[key_index % len(klucz)]) - ord('A')

            zaszyfrowana_wartosc = (wartosc_litery + wartosc_klucza) % 26
            zaszyfrowana_litera = chr(zaszyfrowana_wartosc + ord('A'))

            wynik += zaszyfrowana_litera
            key_index += 1
        else:
            wynik += litera

    return wynik


def test_vigenere():
    tekst = "HELLO WORLD"
    klucz = "KEY"
    wynik = szyfruj_vigenere(tekst, klucz)

    print("=== Szyfr Vigenere'a ===")
    print("Tekst:", tekst)
    print("Klucz:", klucz)
    print("Wynik:", wynik)


if __name__ == "__main__":
    test_vigenere()
