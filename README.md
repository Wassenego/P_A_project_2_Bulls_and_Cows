# P_A_project_2_Bulls_and_Cows
Python Academy project 2 - Bulls and Cows - druhý projekt na Python akademii na Engeto.

## Popis projektu
V tomto projektu jsem měli za úkol vytvořit hru Bulls and Cows, v Česku známější jako Logik, při které se hráč snaží pomocí nápovědy uhodnout správnou kombinaci čísel. 

*(Oproti původnímu pevně danému počtu hádaných číslic chci ještě program upravit tak, aby si hráč může zvolit, kolikati-ciferný kód bude hádat v rozmezí 2-10.)*

## Instalace knihoven
Pro hru byly použity jen built-in knihovny, nebylo potřeba tvořit virtuální prostředí ani soubour requirements.txt

## Spuštění projektu
Spuštění projektu lze bez nutnosti vkládaní argumentů.

## Program obsahuje
- vytvoření tajného 4-místného čísla (číslice musí být unikátní a kód nesmí začínat 0). *(Počet hádaných čísel se v další verzi bude dát volit.)*

- pozdravení užitele a vypsání úvodního textu
    ```
    Hi there!
    ------------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a 'Bulls and Cows' game.
    ------------------------------------------------
    ```
- žádost o vložení prvního 4-místného čísla. Program hráče upozorní:
     - pokud zadá číslo kratší nebo delší než 4 číslice, příp. obsahovat nečíselné znaky.
    - pokud bude obsahovat duplicity.
    - pokud bude začínat nulou.


- vyhodnocení tipu uživatele po každém hádání. Vypsání počtu bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení bere ohled na jednotné a množné číslo ve výstupu.
    ```
    >>> 1358
    1 bull, 1 cow
    ---------------------------------
    >>> 5683
    0 bulls, 2 cows
    ---------------------------------
    ```

- po uhodnutí tajného čísla program hráči pogratuluje a vyhodnotí ho podle počtu pokusů. Program spočítá celkovou dobu hádání.
    ```
    Correct, you've guessed the right number in 3 attempts!
    Your total time of guessing took 0 minutes and 9 seconds.

                      That's brilliant.
    ```
- vyhodnocením hra končí a program se ukončí




