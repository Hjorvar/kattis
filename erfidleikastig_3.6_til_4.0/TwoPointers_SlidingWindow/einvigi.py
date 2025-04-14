import sys

# Aðgerðir fyrir innlestur
def input():
    return sys.stdin.readline().strip()

def input_int_list():
    return list(map(int, input().split()))

# --- Innlestur ---
n, m, k = input_int_list()
a = input_int_list() # Styrkur Tómasar
b = input_int_list() # Styrkur andstæðings

# --- Forreikningur: Útkomur einvígja ---
# Concept 2: Arrays/Lists - Geymum niðurstöður í listum.
# Reiknum útkomu (+1, -1, 0) fyrir hvert einvígi BÆÐI með og án styrkingar.
# Tímaflækja: O(N)
outcome_normal = [0] * n
outcome_boosted = [0] * n

for i in range(n):
    # Venjuleg útkoma
    if a[i] > b[i]:
        outcome_normal[i] = 1
    elif a[i] < b[i]:
        outcome_normal[i] = -1
    # else: outcome_normal[i] = 0 (sjálfgefið)
    
    # Útkoma með styrkingu
    if a[i] + k > b[i]:
        outcome_boosted[i] = 1
    elif a[i] + k < b[i]:
        outcome_boosted[i] = -1
    # else: outcome_boosted[i] = 0 (sjálfgefið)

# --- Grunnstaða og fyrsti gluggi ---
# Reiknum heildar "stig" án styrkingar. Jákvætt = Tómas vinnur fleiri.
# Tímaflækja: O(N)
base_score = sum(outcome_normal)

# Reiknum stigin fyrir fyrsta mögulega gluggann (s=0)
# Tímaflækja: O(M)
current_score = base_score
for i in range(m):
    current_score -= outcome_normal[i]  # Fjarlægjum venjulega útkomu
    current_score += outcome_boosted[i] # Bætum við styrktri útkomu

# Athugum hvort s=0 sé lausn
# Sigur er ef current_score > 0 (Tómas vann fleiri einvígi)
if current_score > 0:
    print(0)
    sys.exit() # Hættum þar sem við fundum fyrstu/minnstu lausn

# --- Rennum Glugganum ---
# Concept 6: Two Pointers / Sliding Window
# Förum með gluggann frá s=1 til n-m. Í hverju skrefi uppfærum við
# 'current_score' á O(1) tíma.
# Tímaflækja: O(N-M) * O(1) = O(N) í heildina.
found_s = -1 # Geymum index ef við finnum lausn
for s in range(1, n - m + 1):
    # Index einvígis sem er að detta ÚT ÚR glugganum (vinstra megin)
    outgoing_idx = s - 1
    # Index einvígis sem er að koma INN Í gluggann (hægra megin)
    incoming_idx = s + m - 1
    
    # Uppfærum 'current_score':
    # 1. Fjarlægjum áhrif styrkingar frá 'outgoing_idx'
    current_score -= outcome_boosted[outgoing_idx]
    # 2. Bætum við venjulegum áhrifum fyrir 'outgoing_idx'
    current_score += outcome_normal[outgoing_idx]
    # 3. Fjarlægjum venjuleg áhrif frá 'incoming_idx'
    current_score -= outcome_normal[incoming_idx]
    # 4. Bætum við áhrifum styrkingar fyrir 'incoming_idx'
    current_score += outcome_boosted[incoming_idx]
    
    # Athugum hvort Tómas vinni núna
    if current_score > 0:
        found_s = s # Fundum lausn! Geymum indexið.
        break # Hættum leit þar sem við viljum LÆGSTA s.

# --- Úttak ---
if found_s != -1:
    print(found_s)
else:
    print("Neibb")

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Forreikningur: O(N)
# Fyrsti gluggi: O(M)
# Rennandi gluggi: O(N-M)
# Heildartímaflækja: O(N + M + N - M) = O(N), sem er nógu hratt.  