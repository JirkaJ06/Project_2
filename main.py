"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jiri Janku
email: janku.jirka@gmail.com
"""

import random

def generuj_cislo(delka):
    """Vygeneruje náhodné 4místné číslo s unikátními číslicemi. Číslo nesmí začínat nulou."""
    cislo = ""
    pouzite = set()
    while len(cislo) < delka:
        cifra = str(random.randint(0, 9))
        if len(cislo) == 0 and cifra == "0":
            continue  # první číslice nesmí být nula
        if cifra not in pouzite:
            cislo += cifra
            pouzite.add(cifra)
    return cislo

def ziskej_byky_a_kravy(tajne, tip):
    """Spočítá počet býků a krav."""
    byci = sum(1 for t, g in zip(tajne, tip) if t == g)  # Počet číslic na správné pozici.
    kravy = sum(1 for g in tip if g in tajne) - byci  # Počet číslic na špatné pozici.
    return byci, kravy

def vypis(text, separator="-" * 40):
    """
    Vypíše text s oddělovačem pro lepší přehlednost.
    """
    separator = '-' * 40    
    print(f"{text}\n{separator}")

def hraj_hru():
    """Hlavní logika hry."""
    tajne_cislo = generuj_cislo(4)  # Vygeneruje tajné číslo.
    pokusy = 0  # Počet pokusů.

    vypis("Hi there!")
    vypis("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    vypis("Enter a number:")

    while True:
        tip = input()
        # Ověření vstupu
        if len(tip) != 4 or not tip.isdigit() or len(set(tip)) != 4 or tip[0] == '0':
            vypis("Invalid input. Please enter a 4-digit number with unique digits and not starting with zero.")
            continue

        pokusy += 1  # Zvýší počet pokusů.
        byci, kravy = ziskej_byky_a_kravy(tajne_cislo, tip)  # Spočítá býky a krávy.

        # Úprava jednotného/množného čísla pro býky a krávy
        text_byci = "bull" if byci == 1 else "bulls"
        text_kravy = "cow" if kravy == 1 else "cows"

        vypis(f"{byci} {text_byci}, {kravy} {text_kravy}")

        if byci == 4:  # Pokud hráč uhodne celé číslo.
            vypis(f"Correct, you've guessed the right number in {pokusy} guesses!")
            vypis("That's amazing!")
            break

if __name__ == "__main__":
    hraj_hru()
