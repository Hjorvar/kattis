import sys

# --- Inntakslestur ---
try:
    line1 = sys.stdin.readline().split()
    n = int(line1[0]) # Fjöldi formúla
    L = int(line1[1]) # Hámarks línufjöldi

    items = [] # Listi til að geyma formúlur
    for i in range(n):
        line_item = sys.stdin.readline().split()
        lines = int(line_item[0])
        value = int(line_item[1])
        # Geymum línur, verðmæti og upprunalegan index (0 til n-1)
        items.append({'lines': lines, 'value': value, 'id': i})

except Exception:
    exit() # Villa við lestur

# --- Dýnamísk Forritun (0/1 Knapsack) ---
# Atriði 12: Dynamic Programming

# dp[i][j] = hámarks verðmæti með fyrstu i hlutunum og plássi j
# Búum til DP töflu af stærð (n+1) x (L+1), fyllta af 0
dp = [[0 for _ in range(L + 1)] for _ in range(n + 1)]

# Atriði 1: Time Complexity - O(N * L) fyrir þessar lykkjur
# Förum í gegnum formúlur i = 1..n
for i in range(1, n + 1):
    # Sækjum upplýsingar um núverandi formúlu (index i-1 í items listanum)
    current_lines = items[i-1]['lines']
    current_value = items[i-1]['value']

    # Förum í gegnum mögulegt pláss j = 0..L
    for j in range(L + 1):
        # Möguleiki 1: Ekki taka formúlu i.
        # Verðmætið er það sama og fyrir i-1 formúlur með plássi j.
        value_without_item = dp[i-1][j]

        # Möguleiki 2: Taka formúlu i (ef hún kemst fyrir: current_lines <= j).
        value_with_item = 0 # Sjálfgefið ef hún kemst ekki fyrir
        if current_lines <= j:
            # Verðmætið er gildi formúlunnar + besta gildið með i-1 formúlum
            # og því plássi sem eftir er (j - current_lines).
            remaining_capacity = j - current_lines
            value_with_item = current_value + dp[i-1][remaining_capacity]

        # dp[i][j] er það hæsta af þessum tveimur möguleikum
        dp[i][j] = max(value_without_item, value_with_item)

# --- Finna hámarks verðmæti ---
max_total_value = dp[n][L]

# --- Bakka (Backtracking) til að finna valdar formúlur ---
chosen_items_indices = []
remaining_capacity = L # Byrjum með fullt pláss

# Förum afturábak frá síðustu formúlu i = n niður í 1
for i in range(n, 0, -1):
    # Athugum hvort hámarksgildið í dp[i][remaining_capacity]
    # hafi krafist þess að formúla i (index i-1) hafi verið notuð.
    # Það gerðist ef gildið er hærra en ef við hefðum *ekki* notað hana (dp[i-1][rem_cap]).
    if dp[i][remaining_capacity] > dp[i-1][remaining_capacity]:
        # Já, formúla i (index i-1) var valin.
        item_index = i - 1
        chosen_items_indices.append(items[item_index]['id'])
        # Minnka plássið sem eftir er.
        remaining_capacity -= items[item_index]['lines']
    # else: Formúla i var ekki valin, höldum áfram með sama pláss.

# Listinn er í öfugri röð, snúum honum við.
chosen_items_indices.reverse()

# --- Úttak ---
# Prenta fjölda valinna hluta og hámarks verðmætið
print(len(chosen_items_indices), max_total_value)
# Prenta indexana á völdum hlutum, aðskilda með bili
print(*(chosen_items_indices))

# --- Endir kóða ---