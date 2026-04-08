def szyfruj_vigenere(tekst, klucz):
    wynik = ""
    key_index = 0
    tekst = tekst.upper()
    klucz = klucz.upper()

    for litera in tekst:
        if 'A' <= litera <= 'Z':
            wartosc_litery = ord(litera) - ord('A')
            wartosc_klucza = ord(klucz[key_index % len(klucz)]) - ord('A')

            # Szyfrowanie: (L + K) % 26
            zaszyfrowana_wartosc = (wartosc_litery + wartosc_klucza) % 26
            wynik += chr(zaszyfrowana_wartosc + ord('A'))
            key_index += 1
        else:
            wynik += litera
    return wynik


def deszyfruj_vigenere(zaszyfrowany_tekst, klucz):
    wynik = ""
    key_index = 0
    zaszyfrowany_tekst = zaszyfrowany_tekst.upper()
    klucz = klucz.upper()

    for litera in zaszyfrowany_tekst:
        if 'A' <= litera <= 'Z':
            wartosc_litery = ord(litera) - ord('A')
            wartosc_klucza = ord(klucz[key_index % len(klucz)]) - ord('A')

            # Deszyfrowanie: (L - K) % 26
            # Python poprawnie obsługuje modulo z liczb ujemnych
            odszyfrowana_wartosc = (wartosc_litery - wartosc_klucza) % 26
            wynik += chr(odszyfrowana_wartosc + ord('A'))
            key_index += 1
        else:
            wynik += litera
    return wynik


if __name__ == "__main__":
    # 1. Dane wejściowe
    oryginalny_tekst = "PROGRAMOWANIE JEST SUPER"
    klucz = "abc"

    # 2. Szyfrowanie
    zaszyfrowany = szyfruj_vigenere(oryginalny_tekst, klucz)

    # 3. Deszyfrowanie
    odszyfrowany = deszyfruj_vigenere(zaszyfrowany, klucz)

    # 4. Sprawdzenie wyników
    print("=== TEST SZYFRU VIGENERE'A ===")
    print(f"Oryginał:    {oryginalny_tekst}")
    print(f"Klucz:       {klucz}")
    print(f"Zaszyfrowany: {zaszyfrowany}")
    print(f"Odszyfrowany: {odszyfrowany}")

    if oryginalny_tekst == odszyfrowany:
        print("\nSUKCES: Tekst odszyfrowany jest identyczny z oryginalnym!")
    else:
        print("\nBŁĄD: Teksty się różnią.")