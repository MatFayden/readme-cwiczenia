def cezar(tekst: str, klucz: int):
    wynik = ""
    for litera in tekst:
            kod_bazowy = 65 if litera.isupper() else 97
            nowy_kod = (ord(litera) - kod_bazowy + klucz) % 26 + kod_bazowy
            wynik += chr(nowy_kod)
    return wynik

print(cezar("haslo", 3))