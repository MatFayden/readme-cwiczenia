def szyfruj_cezara(tekst: str, klucz: int) -> str:
    wynik = ""

    for litera in tekst:
        if litera.isalpha():
            kod_bazowy = 65 if litera.isupper() else 97
            nowy_kod = (ord(litera) - kod_bazowy + klucz) % 26 + kod_bazowy
            wynik += chr(nowy_kod)
        else:
            wynik += litera

    return wynik


if __name__ == "__main__":
    print(szyfruj_cezara("HASLO", 3))
