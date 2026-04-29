# Szyfr Vigenère'a

Szyfr Vigenère'a to metoda szyfrowania tekstu alfabetycznego za pomocą serii różnych szyfrów Cezara opartych na literach słowa kluczowego.

## Działanie
Klucz jest powtarzany tyle razy, ile liter ma tekst jawny. Każda litera tekstu jest przesuwana o wartość odpowiadającej jej litery klucza.

## Funkcje w kodzie

### `szyfruj_vigenere(tekst, klucz)`
Szyfruje tekst przy użyciu słowa kluczowego.
- **Argumenty:**
  - `tekst` (str): Tekst jawny.
  - `klucz` (str): Słowo kluczowe (tylko litery).
- **Zwraca:** Zaszyfrowany string (WIELKIE LITERY).

### `deszyfruj_vigenere(tekst, klucz)`
Odszyfrowuje tekst przy użyciu słowa kluczowego.
- **Argumenty:**
  - `tekst` (str): Szyfrogram.
  - `klucz` (str): Słowo kluczowe.
- **Zwraca:** Odszyfrowany string (WIELKIE LITERY).

## Przykład użycia
```python
from vigenere import szyfruj_vigenere

# Szyfrowanie
tajne = szyfruj_vigenere("HELLO", "KEY")
print(tajne) # RIJVS
```
