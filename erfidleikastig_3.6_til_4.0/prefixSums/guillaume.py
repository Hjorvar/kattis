import sys

# Aðgerð til að lesa eina línu
def input():
    return sys.stdin.readline().strip()

# Lesum fjölda leikja
n = int(input())
# Lesum leikjarununa
games = input()

# --- Forreikningur: Prefix Sums ---
# Concept 7: Prefix Sums
# Búum til fylki til að geyma uppsafnaðan fjölda sigra og gildra leikja.
# Stærð n+1 til að einfalda útreikninga (index 0 er 0).
# Tímaflækja: O(N)
prefix_g = [0] * (n + 1)
prefix_a = [0] * (n + 1)
prefix_valid = [0] * (n + 1) # Telur A og G

for i in range(n):
    # Afritum fyrra gildi
    prefix_g[i+1] = prefix_g[i]
    prefix_a[i+1] = prefix_a[i]
    prefix_valid[i+1] = prefix_valid[i]
    
    # Uppfærum ef við á
    if games[i] == 'G':
        prefix_g[i+1] += 1
        prefix_valid[i+1] += 1
    elif games[i] == 'A':
        prefix_a[i+1] += 1
        prefix_valid[i+1] += 1

# --- Finnum besta k ---
# Upphafsstillum breytur fyrir bestu niðurstöðu.
# Notum best_g = -1 og best_valid = 1 til að tákna "verra en 0%" hlutfall í byrjun.
best_g = -1 
best_valid = 1
min_k = n + 1 # Minnsta k sem gefur besta hlutfallið
final_g = 0   # Sigrar G í besta kaflanum
final_a = 0   # Sigrar A í besta kaflanum

# Förum í gegnum allar mögulegar lengdir k á lokakaflanum.
# Concept 1: Time Complexity - Þessi lykkja er O(N).
for k in range(1, n + 1):
    # Reiknum fjölda G, A og gildra leikja í síðustu k leikjum með Prefix Sums.
    # Aðgerðirnar hér inni taka O(1) tíma.
    g_k = prefix_g[n] - prefix_g[n-k]
    a_k = prefix_a[n] - prefix_a[n-k]
    valid_k = prefix_valid[n] - prefix_valid[n-k]
    
    # Ef engir gildir leikir eru í þessum kafla, getur hann ekki verið sá besti
    # (nema allir kaflar séu þannig, en þá viljum við minnsta k, sem k=1 hefði séð um ef gilt).
    # Við gerum ráð fyrir að besta hlutfallið verði >= 0.
    if valid_k == 0:
        # Ef besta hingað til er líka 0% (best_g <= 0), og þetta k er minna, uppfærum.
        # Annars sleppum við þessu k.
        # Einföldun: Ef besta er < 0, þá er 0/0 betra ef k er minna.
        # Ef besta er >= 0, þá er 0/0 ekki betra.
        if best_g < 0: # Ef ekkert gilt hefur fundist ennþá
             if k < min_k: # Viljum minnsta k, jafnvel fyrir 0-0
                 min_k = k
                 final_g = 0
                 final_a = 0
                 # best_g/best_valid helst -1/1 eða verður 0/1 ef þetta er fyrsta k
                 if best_g < 0: 
                     best_g = 0 
                     best_valid = 1 # Táknar 0% með gilt nefnara
        continue # Förum í næsta k
        
    # Berum saman núverandi hlutfall (g_k / valid_k) við besta hlutfall hingað til (best_g / best_valid)
    # Notum krossmargföldun til að forðast flotölur og tryggja nákvæmni.
    # Ath: best_valid er alltaf >= 1 hér.
    # Er g_k / valid_k > best_g / best_valid ? -> g_k * best_valid > best_g * valid_k
    is_better = (g_k * best_valid > best_g * valid_k)
    # Er g_k / valid_k == best_g / best_valid ? -> g_k * best_valid == best_g * valid_k
    is_equal = (g_k * best_valid == best_g * valid_k)
    
    # Uppfærum ef núverandi er betra, EÐA ef það er jafnt OG k er minna.
    if is_better or (is_equal and k < min_k):
        best_g = g_k
        best_valid = valid_k
        min_k = k
        final_g = g_k
        final_a = a_k

# --- Úttak ---
# Prentum sigrana úr besta kaflanum sem fannst.
print(f"{final_g}-{final_a}")

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Forreikningur Prefix Sums: O(N)
# Leit að besta k: O(N) með O(1) aðgerðum í hverri ítrun.
# Heildartímaflækja: O(N) + O(N) = O(N). Mjög skilvirkt.