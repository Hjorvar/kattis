import sys

# Fall til að lesa tvær heiltölur
def input_int_pair():
    return map(int, sys.stdin.readline().strip().split())

# Lesum inn fjölda raða (r) og dálka (d)
r, d = input_int_pair()

# --- Greining byggð á lögun hnitanetsins ---
# Concept 13: Basic Graph Theory - Við greinum tvö megin tilfelli: 1D (lína) og 2D (rétthyrningur).

# Tilfelli 1: Netið er ein vídd (annað hvort r=1 eða d=1)
if r == 1 or d == 1:
    # Heildarfjöldi reita/hnúta
    cells = r * d 
    # Fyrir línu með V hnúta er styttsta leiðin til að fara enda á milli 
    # og til baka nákvæmlega 2*(V-1) skref. Þetta á við um alla nema 1x1.
    if cells == 1: # Sérhöndlum 1x1 tilfellið
         result = 0 
    else:
         result = 2 * (cells - 1)

# Tilfelli 2: Netið er tvívítt (r > 1 og d > 1)
else:
    cells = r * d
    # Hér notum við odda/sléttutölu rök (parity argument) fyrir 2D net.
    # Lokuð ganga sem byrjar og endar á sama reit verður að hafa jafnan fjölda skrefa.
    
    # Ef heildarfjöldi reita er oddatala (BÆÐI r og d eru oddatölur)
    if r % 2 != 0 and d % 2 != 0: 
        # Lágmarkslengd til að heimsækja alla er 'cells' (oddatala).
        # Styttsta JAFNA lengd sem er >= cells er cells + 1.
        result = cells + 1
    # Ef heildarfjöldi reita er slétt tala (a.m.k. önnur víddin slétt)
    else:
        # Lágmarkslengd er 'cells' (slétt tala). Hægt er að finna göngu af þessari lengd.
        result = cells

# Prentum út niðurstöðuna
# Concept 1: Time Complexity - Lausnin er O(1) eftir innlestur.
print(result)