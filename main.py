import cezar
from vigenere import szyfruj_vigenere
import secrets
import string
import time

def generuj_klucz(rodzaj, dlugosc=10):
    if rodzaj == "cezar":
        return secrets.choice(range(1, 26))
    elif rodzaj == "vigenere":
        return ''.join(secrets.choice(string.ascii_uppercase) for _ in range(dlugosc))
    else:
        raise ValueError("Nieznany rodzaj szyfru")

def main():
    print("Autorzy programu: AI Assistant")
    print("Obsługiwane szyfry: Cezara, Vigenere'a")

    tekst = "PROGRAMOWANIE W PYTHONIE JEST CIEKAWE!"
    
    # Cezar
    klucz_cezar = generuj_klucz("cezar")
    start = time.perf_counter()
    wynik_cezar = cezar.cezar(tekst, klucz_cezar)
    koniec = time.perf_counter()
    czas_cezar = koniec - start
    
    print(f"\n=== Szyfr Cezara ===")
    print(f"Tekst: {tekst}")
    print(f"Klucz: {klucz_cezar}")
    print(f"Wynik: {wynik_cezar}")
    print(f"Czas:  {czas_cezar:.6f}s")

    # Vigenere
    klucz_vigenere = generuj_klucz("vigenere", 5)
    start = time.perf_counter()
    wynik_vigenere = szyfruj_vigenere(tekst, klucz_vigenere)
    koniec = time.perf_counter()
    czas_vigenere = koniec - start
    
    print(f"\n=== Szyfr Vigenere'a ===")
    print(f"Tekst: {tekst}")
    print(f"Klucz: {klucz_vigenere}")
    print(f"Wynik: {wynik_vigenere}")
    print(f"Czas:  {czas_vigenere:.6f}s")
    
    print(f"\nPorównanie czasów: {'Vigenere wolniejszy' if czas_vigenere > czas_cezar else 'Cezar wolniejszy'}")

if __name__ == "__main__":
    main()
