import sys

# --- Inntakslestur ---
try:
    line1 = sys.stdin.readline().split()
    n = int(line1[0])
    p_per_day = int(line1[1])

    # Lesa listann af a_i gildum
    a = list(map(int, sys.stdin.readline().split()))

    # Athuga hvort fjöldi gilda passi við n
    if len(a) != n:
        exit() # Villa í inntaki

except Exception:
    exit() # Villa við lestur eða umbreytingu

# --- Útreikningar ---

# Reikna S = sum(a_i)
# O(n) tími
total_names = sum(a)

# Reikna Sq = sum(a_i^2)
# O(n) tími
sum_of_squares = sum(x*x for x in a)

# Reikna heildarfjölda gildra para með formúlunni
# total_valid_pairs = (S^2 - Sq) / 2
# Notum heiltöludeilingu '//' fyrir síðasta skrefið
total_valid_pairs = (total_names * total_names - sum_of_squares) // 2

# --- Reikna fjölda daga ---

# Nota loftið (ceiling) af deilingunni
# Dagar = ceil(TotalValidPairs / P)
# Útfært með heiltöludeilingu: (teljari + nefnari - 1) // nefnari
# Meðhöndla jaðartilfelli: ef engin pör eru, þá 0 dagar.
# Og ef P <= 0 (þó það sé útilokað af skilyrðum, gott að hafa í huga)

days_needed = 0
if total_valid_pairs > 0:
    # Athuga hvort P sé gilt (þó skilyrði segi 1 <= P)
    if p_per_day > 0:
        days_needed = (total_valid_pairs + p_per_day - 1) // p_per_day
    # else: Dagar væru óendanlegir ef P=0 og pör > 0
# Ef total_valid_pairs == 0, þá helst days_needed sem 0.

# --- Úttak ---
print(days_needed)

# --- Endir kóða ---