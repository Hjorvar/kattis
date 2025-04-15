import sys

# Aðgerðir fyrir (mögulega) hraðari innlestur
def input():
    return sys.stdin.readline().strip()

def input_int_list():
    return list(map(int, input().split()))

# --- Innlestur ---
n, m = input_int_list()
grill_times = input_int_list()

# Heildarfjöldi borgara sem þarf að elda
# Ef m=0, þurfum við 1 borgara (fyrir Benna). M >= 1 alltaf.
M = m + 1 

# --- Tvíundarleit yfir svarið (Tíminn T) ---
# Concept 5: Binary Search (Binary Search the Answer)
# Við leitum að minnsta tíma T þar sem hægt er að elda M borgara.
# Fallið check(T) = (fjöldi eldaðra borgara á tíma T) er einhæft vaxandi.

# Setjum leitarsvið fyrir T.
low = 0 
# Efsta mark: Ef við notum hraðasta grillið (tími 1) þyrfti M tíma.
# Ef við notum hægasta grillið (max_t) þyrfti M * max_t tíma.
# Veljum mjög hátt efra mark til öryggis (max_t * M getur orðið 10^18)
# Python sér um stórar heiltölur.
# Finnum hæsta grill tíma til að fá raunhæfara efra mark
max_t = 0
for t in grill_times:
    if t > max_t:
        max_t = t
# Öruggt efra mark, passar í 64-bita tölu
high = max_t * M 
# Geymum besta svarið sem við finnum (minnsti tími T sem virkar)
ans = high 

# Concept 1: Time Complexity - Lykkjan keyrir O(log R) sinnum, þar sem R = high.
while low <= high:
    # Reiknum miðpunkt til að athuga
    mid = low + (high - low) // 2 
    
    # --- Athugunarfall (check(mid)) ---
    # Reiknum hversu marga borgara er hægt að klára á 'mid' sekúndum.
    # Tímaflækja: O(N) þar sem við förum yfir öll grillin.
    cooked_burgers = 0
    for time_i in grill_times:
        # Passa upp á deilingu með 0 ef time_i gæti verið 0 (ekki skv. lýsingu)
        if time_i > 0:
            cooked_burgers += mid // time_i
        # Valfrjálst: Hætta snemma ef við erum komin yfir M? 
        # Getur flýtt örlítið en breytir ekki O(N) flækju checksins.
        # if cooked_burgers >= M:
        #     break 
            
    # --- Ákvörðun í tvíundarleit ---
    # Ef við náðum að elda nógu marga borgara (eða fleiri)
    if cooked_burgers >= M:
        # Þá er 'mid' möguleg lausn. Prófum hvort við finnum enn betri (minni) tíma.
        ans = mid # Geymum þessa mögulegu lausn
        high = mid - 1 # Leitum í neðri helmingnum
    else:
        # Ef við náðum EKKI að elda nógu marga borgara
        # Þá þurfum við meiri tíma.
        low = mid + 1 # Leitum í efri helmingnum

# --- Úttak ---
# 'ans' geymir nú minnsta tímann T þar sem fjöldi borgara >= M.
print(ans)

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Heildartímaflækja: O(N * log R), þar sem N er fjöldi grilla og R er efra mark tímans.
# Þetta er mjög skilvirkt og ætti að standast tímamörk.