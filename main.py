import cezar
from vigenere import szyfruj_vigenere


def main():
    print("Autorzy programu: osoba od Cezara, osoba od Vigenere'a")
    print("Obsługiwane szyfry: Cezara, Vigenere'a")

    tekst = "HELLO WORLD"

    print("\n=== Test szyfru Cezara ===")
    print("Tekst:", tekst)
    print("Klucz:", 3)
    print("Wynik:", cezar.cezar(tekst, 3))

    print("\n=== Test szyfru Vigenere'a ===")
    print("Tekst:", tekst)
    print("Klucz:", "KEY")
    print("Wynik:", szyfruj_vigenere(tekst, "KEY"))


if __name__ == "__main__":
    main()
