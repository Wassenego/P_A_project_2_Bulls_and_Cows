"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls and cows
author: Marek Sýkora
email: MarekSykora78@seznam.cz
discord: Wassenego#1875
"""
import random
import time

# definování funkce ke generování hledaného čísla tak, aby splňovalo všechny podmínky.
def generuj_tajne_cislo(delka: int) -> str:
    """
    Popis:
    - generuje tajné číslo, které musí uživatel ve hře uhodnout.
    Parametry:
    - delka (int): Požadovaná délka tajného čísla. 
    Návratová hodnota:
    - string : Tajné číslo vygenerované jako řetězec, které je výhodnější pro další kontrolu ve hře. 
    """
    generovane_cislice = []
    while len(generovane_cislice) != delka_cisla:
        cislice = str(random.randrange(10))
        if (cislice == "0" and generovane_cislice == []) or cislice in generovane_cislice:
            continue
        else:
            generovane_cislice.append(cislice)

    tajne_cislo = "".join(generovane_cislice)
    return tajne_cislo

# definování funkce, která vytiskne hodnocení hry na základě počtu pokusů k určení správného čísla
def hodnot_vykon_hrace(pocet: int) -> str:
    """
    Popis:
    - hodnotí výkon hráče na základě počtu pokusů k dohrání hry 'Bulls and Cows'. 
    Parametry:
    - pocet (int): Počet pokusů, které hráč provedl.
    Návratová hodnota:
    - str: Slovní ohodnocení výkonu hráče.
    """
    hodnoceni = {(1,):"unbelievable. You were born under a lucky star", (2, 3):"brilliant",
                 (4, 5):"amazing", (6, 7):"average", (8, 9):"not so good",
                 (10, 11):"poor", (12," a víc"):"useless"}
    if pocitani_poctu_pokusu[0] > 11:
        vysledek = hodnoceni[(12," a víc")]
    else:
        for klic in hodnoceni:
            if pocet in klic:
                (vysledek := hodnoceni[klic])
    
        return print(f"That's {vysledek}.".center(61))

# definování funkce, která bude hlídat gramaticky správné tisknutí anglických slov v závislosti na množném či jednotném číslu    
def gramatika(promenna: list) -> str:
    """
    Popis:
    - funkce, která pro proměnné, jejichž číselná hodnota se vypisuje v textu, pohlídá, aby se slovo za číselnou hodnotou
      vypsalo ve správné gramatické podobě     
    Parametry:
    - promenna (list): proměnná, jejíž hodnota je seznam, kdy na indexu[0] je číslo (int), které se může měnit podle průběhu hry,
      na indexu[1] je správná gramatická podoba slova v jednotném čísle a na posledním indexu je správná gramatická podoba slova 
      v množném čísle
    Návratová hodnota:
    - str: Správně vypsaná podoba slova, aby v textu nebyla grmatická chyba.
    """
    if promenna[0] == 1:
        return promenna[1]
    else:
        return promenna[2]
    
delka_cisla = 4 # volitelná hodnota, je možnost zadat jinou délku hledaného čísla (maximálně 10 číslic)
oddelovac = "-" * 61

tajne_cislo = generuj_tajne_cislo(delka_cisla)

# jde si vytisknout hledané číslo pro kontrolu
# print(tajne_cislo) 

uvod = f"""\
I've generated a random {delka_cisla} digit number for you.
Let's play a 'Bulls and Cows' game.\
"""
print("Hi there!", oddelovac, uvod, oddelovac, "Enter a number:", oddelovac,sep="\n")

pocitani_poctu_pokusu = [1, "attempt", "attempts"]
zacatek_hry = time.time() # spuštění stopek.


#  ověření, zda je hráčem zadaná hodnota v mezích pravidel
    # číslo musí mít délku, která je definovaná na začátku kódu a zmíněná v úvodním uvítání hráče
    # nesmí začínat nulou a obsahovat jiné znaky než číslice
    # číslo nesmí obsahovat duplicitní číslice

while (vstup := input(">>> ")) != tajne_cislo:
    if not vstup.isdigit() or len(vstup) != delka_cisla:
        print(f"Tvůj vstup neobsahuje {delka_cisla}-místné číslo, zkus to znovu.")
        print(oddelovac)
        continue
    elif len(set(vstup)) < delka_cisla:
        print(f"Tvůj vstup obsahuje duplicitní hodnoty číslic, zkus to znovu.")
        print(oddelovac)
        continue
    else:
        int(vstup)
  
    # je otázkou, zda se má nesprávně zadaná hodnota počítat do počtu pokusů. Rozhodl jsem se, že ji počítat nebudu,
    # jelikož hráč nedostane žádnou nápovědu a mohl se jen překlepnout. Pokud by se nesprávné zadání mělo počítat,
    # přesunulo by se počítání hned za úvodní řádek smyčky s podmínkou

    # ověřování hráčem zadaného čísla 
    bulls = [0, "bull", "bulls"]
    cows = [0, "cow", "cows"]

    for pozice in range(4):
        if vstup[pozice] == tajne_cislo[pozice]:
            bulls[0] += 1
        elif vstup[pozice] in tajne_cislo:
            cows[0] += 1
        else:
            continue

    pocitani_poctu_pokusu[0] += 1

    # tisknutí nápovědy hráči 
    print(f"{bulls[0]} {gramatika(bulls)}, {cows[0]} {gramatika(cows)}")
    print(oddelovac)

# ukončení hry po uhádnutí hledaného čísla
else:
    # zastavení stopek a příprava pro tisk 
    konec_hry = time.time()
    doba_hadani = int(konec_hry - zacatek_hry)
    minutes = [0, "minute", "minutes"]
    minutes[0] += doba_hadani // 60
    seconds = [0, "second", "seconds"]
    seconds[0] += doba_hadani % 60

# tisk vyhodnocení počtu pokusů a doby hádání
    print(f"""\
Correct, you've guessed the right number in {pocitani_poctu_pokusu[0]} {gramatika(pocitani_poctu_pokusu)}!
Your total time of guessing took {minutes[0]} {gramatika(minutes)} and {seconds[0]} {gramatika(seconds)}.
"""
)

# slovní hodnocení hráče podle počtu pokusů pomocí funkce 'hodnot_vykon_hrace(pocet)'
vysledek = hodnot_vykon_hrace(pocitani_poctu_pokusu[0])
print(oddelovac)
