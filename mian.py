"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jiri Janku
email: janku.jirka@gmail.com
"""

import random

separator = '-' * 40

def generuj_cislo():
    """Vygeneruje náhodné 4místné číslo s unikátními číslicemi."""
    cislice = list(range(10))  # Vytvoří seznam číslic od 0 do 9.
    random.shuffle(cislice)  # Náhodně promíchá pořadí číslic.
    return ''.join(map(str, cislice[:4]))  # Vezme první 4 číslice, převede je na řetězec a spojí je.

def ziskej_byky_a_kravy(tajne, tip):
    """Spočítá počet býků a krav."""
    byci = sum(1 for t, g in zip(tajne, tip) if t == g)  # Počet číslic na správné pozici.
    kravy = sum(1 for g in tip if g in tajne) - byci  # Počet číslic na špatné pozici.
    return byci, kravy

def hraj_hru():
    """Hlavní logika hry."""
    tajne_cislo = generuj_cislo()  # Vygeneruje tajné číslo.
    pokusy = 0  # Počet pokusů.

    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)
    print("Enter a number:")
    print(separator)

    while True:
        tip = input()
        # Ověření vstupu
        if len(tip) != 4 or not tip.isdigit() or len(set(tip)) != 4 or tip[0] == '0':
            print("Invalid input. Please enter a 4-digit number with unique digits and not starting with zero.")
            print(separator)
            continue

        pokusy += 1  # Zvýší počet pokusů.
        byci, kravy = ziskej_byky_a_kravy(tajne_cislo, tip)  # Spočítá býky a krávy.

        # Úprava jednotného/množného čísla pro býky a krávy
        text_byci = "bull" if byci == 1 else "bulls"
        text_kravy = "cow" if kravy == 1 else "cows"

        print(f"{byci} {text_byci}, {kravy} {text_kravy}")
        print(separator)

        if byci == 4:  # Pokud hráč uhodne celé číslo.
            print("Correct, you've guessed the right number {pokusy} pokusů.")
            print(f"in {pokusy} guesses!")
            print(separator)
            print("That's amazing!")
            break

if __name__ == "__main__":
    hraj_hru()