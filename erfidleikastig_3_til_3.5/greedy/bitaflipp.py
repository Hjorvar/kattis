import sys

# --- Inntakslestur ---
try:
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split())) # Lesa upphaflega 0 og 1
    if len(a) != n:
        exit() # Villa ef lengd passar ekki
except Exception:
    exit() # Villa við lestur/umbreytingu

# --- Upphafsástand ---
# Reikna upphaflegan fjölda 1-a
initial_ones = sum(a)

# --- Hámarka Breytingu með Greedy/Sliding Window (Kadane's) ---
# Markmið: Finna svæði [i, j] sem hámarkar (Fjöldi 0-a) - (Fjöldi 1-a)
# Umbreyting: 0 -> +1 (hagnaður), 1 -> -1 (tap). Finnum max hlutsummu (max_gain).

# Atriði 8: Greedy Algorithms & Atriði 6: Sliding Window
# Kadane's algóritminn notar græðgisnálgun í hverju skrefi.
# Hann heldur utan um bestu summu sem endar í núverandi stöðu,
# og ákveður græðgislega hvort lengja eigi fyrra svæði eða byrja nýtt.
# Þetta stýrir implicit "glugga" sem táknar núverandi besta svæðið.
# (Þetta er líka náskylt Atriði 12: Dynamic Programming).
# Atriði 1: Time Complexity er O(N).

max_gain_so_far = -float('inf') # Heildar hámarks hagnaður (max hlutsumma)
current_gain_ending_here = 0    # Hámarks hagnaður fyrir svæði sem ENDAR hér

# Jaðartilfelli fyrir tómt inntak (N>=1 skv. lýsingu)
if n == 0:
    print(0)
    exit()

# Förum í gegnum listann (glugginn færist)
for k in range(n):
    # Reiknum "gildið" fyrir þessa stöðu: +1 fyrir 0, -1 fyrir 1
    value = 1 if a[k] == 0 else -1

    # Græðgislegt val / DP skref:
    # Er betra að byrja nýtt svæði hér (gildi=value) eða
    # lengja besta svæðið sem endaði á k-1 (gildi=current_gain_ending_here + value)?
    current_gain_ending_here = max(value, current_gain_ending_here + value)

    # Uppfærum besta heildarárangur (hagnað) sem sést hefur hingað til
    max_gain_so_far = max(max_gain_so_far, current_gain_ending_here)

# max_gain_so_far inniheldur nú hæsta mögulega hagnaðinn (max hlutsummu)
# sem fæst með því að snúa einu samliggjandi svæði [i, j].
max_gain = max_gain_so_far

# --- Lokaniðurstaða ---
# Hámarks lokafjöldi 1-a = Upphafsfjöldi + Hámarks hagnaður
final_max_ones = initial_ones + max_gain

print(final_max_ones)

# --- Endir kóða ---