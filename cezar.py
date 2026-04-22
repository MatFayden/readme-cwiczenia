import string

def cezar(napis: str, klucz: int) -> str:
    if not isinstance(napis, str) or not isinstance(klucz, int):
        raise TypeError("zły typ danych")
    
    wynik = ""
    for litera in napis:
        if litera.isalpha():
            # Ujednolicenie wielkości liter do wielkich (zgodnie z sugestią o zmianie wielkości)
            litera_up = litera.upper()
            kod_bazowy = ord('A')
            nowy_kod = (ord(litera_up) - kod_bazowy + klucz) % 26 + kod_bazowy
            wynik += chr(nowy_kod)
        else:
            wynik += litera
    return wynik

def analiza_czestotliwosci(napis: str) -> int:
    # Częste litery w języku polskim
    czeste_litery = "aieozn"
    punkty = 0
    for litera in napis.lower():
        if litera in czeste_litery:
            punkty += 1
    return punkty

def lamanie_cezara(napis: str) -> str:
    najlepszy_wynik = -1
    najlepszy_tekst = ""
    
    for klucz in range(26):
        # Deszyfrowanie to szyfrowanie z ujemnym kluczem
        probowany_tekst = cezar(napis, -klucz)
        punkty = analiza_czestotliwosci(probowany_tekst)
        
        if punkty > najlepszy_wynik:
            najlepszy_wynik = punkty
            najlepszy_tekst = probowany_tekst
            
    return najlepszy_tekst

if __name__ == "__main__":
    test = "ZALZ"
    print(f"Szyfrowanie 'ALFA' klucz 3: {cezar('ALFA', 3)}")
    print(f"Łamanie 'ZALZ': {lamanie_cezara(test)}")
