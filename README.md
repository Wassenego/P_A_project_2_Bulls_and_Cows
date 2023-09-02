# P_A_project_2_Bulls_and_Cows
Python Academy project 2 - Bulls and Cows - druhý projekt na Python akademii na Engeto.

## Popis projektu
V tomto projektu jsem měli za úkol vytvořit hru Bulls and Cows, v Česku známější jako Logik, při které se hráč snaží pomocí nápovědy uhodnout správnou kombinaci čísel. 
Oproti původnímu požadovanému 4-místnému kódu jsem program upravil tak, aby si hráč mohl zvolit, kolikaticiferný kód bude hádat - rozmezí 2-10.

## Instalace knihoven
Pro hru byly použity jen built-in knihovny, nebylo potřeba tvořit virtuální prostředí ani soubour requirements.txt

## Spuštění projektu
Spuštění projektu `main.py` v rámci příkazového řádku požaduje jeden povinný argument.
```python
python main.py <volena-delka-tajneho-cisla>
```

## Program obsahuje
- vytvoření tajného x-místného čísla (číslice musí být unikátní a kód nesmí začínat 0). 

- pozdravení užitele a vypsání úvodního textu
    ```
    Hi there!
    ------------------------------------------------
    I've generated a random 4-digit number for you.
    Let's play a 'Bulls and Cows' game.
    ------------------------------------------------
    ```
- žádost o vložení prvního x-místného čísla. Program hráče upozorní:
    - pokud zadané číslo bude kratší nebo delší než zvolený počet číslic, příp. obsahovat nečíselné znaky.
    - pokud bude obsahovat duplicitní číslice.
    - pokud bude začínat nulou.

- vyhodnocení tipu uživatele po každém hádání. Vypsání počtu bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cow/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení bere ohled na jednotné a množné číslo ve výstupu.
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




