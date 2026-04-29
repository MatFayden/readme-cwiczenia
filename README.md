# Projekt Szyfrowania (Cezar & Vigenère)

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

Ten projekt zawiera implementację dwóch klasycznych szyfrów: szyfru Cezara oraz szyfru Vigenère'a w języku Python. Projekt został przygotowany w celach edukacyjnych, demonstrując podstawy kryptografii oraz dobrych praktyk programistycznych (testy, dokumentacja, CI).

## Funkcje projektu

- **Szyfr Cezara:**
  - Szyfrowanie z dowolnym przesunięciem.
  - Automatyczne łamanie szyfru metodą analizy częstotliwościowej (zoptymalizowane pod język polski).
- **Szyfr Vigenère'a:**
  - Szyfrowanie i deszyfrowanie za pomocą słowa kluczowego.
  - Obsługa znaków specjalnych i spacji.
- **Generator Kluczy:**
  - Automatyczne generowanie bezpiecznych, losowych kluczy.
- **Testy:**
  - Pełne pokrycie kodu testami jednostkowymi (pytest).

## Instalacja

Wymagany Python 3.10+ oraz biblioteka `pytest`.

```bash
pip install pytest pytest-cov
```

## Użycie

Uruchomienie głównego programu z demonstracją:

```bash
python main.py
```

Uruchomienie testów:

```bash
pytest
```

## Dokumentacja

Szczegółowa dokumentacja znajduje się w folderze `docs/`:
- [Szyfr Cezara](docs/cezar.md)
- [Szyfr Vigenère'a](docs/vigenere.md)

---
*Autorzy: AI Assistant & Współpracownicy*
