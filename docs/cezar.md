# Szyfr Cezara

Szyfr Cezara to jedna z najprostszych technik szyfrowania. Polega na przesunięciu każdej litery alfabetu o stałą liczbę miejsc.

## Działanie
W naszej implementacji szyfr ujednolica wielkość liter (wszystkie na wielkie) i zachowuje znaki specjalne (spacje, znaki interpunkcyjne) w ich oryginalnej formie.

## Funkcje w kodzie

### `cezar(napis, klucz)`
Główna funkcja szyfrująca/deszyfrująca.
- **Argumenty:**
  - `napis` (str): Tekst wejściowy.
  - `klucz` (int): Przesunięcie (dodatnie dla szyfrowania, ujemne dla deszyfrowania).
- **Zwraca:** Zaszyfrowany string.

### `lamanie_cezara(napis)`
Funkcja próbująca odgadnąć tekst bez znajomości klucza.
- **Argumenty:** `napis` (str): Zaszyfrowany tekst.
- **Zwraca:** Najbardziej prawdopodobny tekst odszyfrowany (na podstawie częstotliwości występowania liter w języku polskim).

## Przykład użycia
```python
from cezar import cezar

# Szyfrowanie
tajne = cezar("Ala ma kota", 3)
print(tajne) # DND PD NRWD
```
