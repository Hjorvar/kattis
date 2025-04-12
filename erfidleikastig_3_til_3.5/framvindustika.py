import sys

# --- Byrjun kóða ---

# Lesa inntak: prósenta (p) og breidd (w)
try:
    line = sys.stdin.readline().strip()
    parts = line.split()
    if len(parts) != 2:
        exit() # Hætta ef inntak er rangt formað
    p = int(parts[0]) # Prósenta (0-100)
    w = int(parts[1]) # Breidd stiku (1 til 10^6)
except Exception:
    exit() # Ef villa kemur við lestur/umbreytingu


# --- Útreikningar ---

# Reikna fjölda '#' tákna. Nota heiltöludeilingu '//'.
num_hashes = (p * w) // 100

# Reikna fjölda '-' tákna.
num_dashes = w - num_hashes

# --- Strengjasmíði ---

# Búa til innihald stikunnar.
bar_content = '#' * num_hashes + '-' * num_dashes

# --- Úttak með f-streng ---

# Setja saman lokastrenginn og prenta út með f-streng.
# Nota '{p:>3}%' til að fá prósentuna hægri-jafnaða í 3 stafa svæði.
print(f"[{bar_content}] | {p:>3}%")

# --- Endir kóða ---