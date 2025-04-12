import sys

# --- Inntakslestur ---
try:
    line1 = sys.stdin.readline().split()
    if len(line1) != 2: raise ValueError("Incorrect number of elements on first line")
    n = int(line1[0])
    m = int(line1[1]) # Breytan heitir 'm' (lágstafur)

    s_line = sys.stdin.readline()
    if not s_line: raise ValueError("Missing second line (string)")
    s = s_line.strip()

    if len(s) != n:
        raise ValueError(f"String length {len(s)} does not match N {n}")
    if n > 0 and (s[0] != '#' or s[-1] != '#'):
        raise ValueError("First or last character is not '#'")
    if m < 1 or m > n:
        raise ValueError("m is out of valid range [1, N]")

except Exception as e:
    # print(f"Input Error: {e}", file=sys.stderr)
    exit()

# --- Jaðartilfelli: Herbergið kemst ekki á milli ---
if m >= n - 1:
    print("Neibb")
    exit()

# --- Formengi (Prefix Sum) fyrir fjölda veggja '#' ---
prefix_hash = [0] * (n + 1)
for k in range(n):
    prefix_hash[k+1] = prefix_hash[k] + (1 if s[k] == '#' else 0)

# --- Finna lágmarksfjölda brotinna veggja fyrir gilda glugga ---
min_walls = float('inf')
found_valid_window = False

# Ítreka 'i' sem 0-index byrjunarreit gluggans s[i...i+m-1]
# i fer frá 1 upp í n-m-1
for i in range(1, n - m):
    # Athuga skilyrði: Veggur fyrir framan (s[i-1]) OG veggur fyrir aftan (s[i+m])
    # LEIÐRÉTT: Nota lágstaf 'm' hér
    if s[i-1] == '#' and s[i+m] == '#':
        found_valid_window = True
        # Reikna fjölda veggja '#' INNAN gluggans s[i...i+m-1] með formengi
        # LEIÐRÉTT: Nota lágstaf 'm' hér líka
        walls_in_window = prefix_hash[i+m] - prefix_hash[i]
        # Uppfæra lágmarkið ef þessi gluggi er betri
        min_walls = min(min_walls, walls_in_window)

# --- Úttak ---
if found_valid_window:
    print(min_walls)
else:
    print("Neibb")

# --- Endir kóða ---