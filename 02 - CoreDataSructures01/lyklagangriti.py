import sys
from collections import deque # Notum deque fyrir O(1) aðgerðir á báðum endum

# Lesum inn aðgerðastrenginn
s = sys.stdin.readline().strip()

# --- Gagnagrindur ---
# Concept 2: Core Data Structures - Notum tvær deque til að tákna textann
# vinstra og hægra megin við bendilinn (cursor).
# vinstri: stafir VINSTRA megin við bendil. Sá síðasti er næst bendlinum.
# hægri: stafir HÆGRA megin við (eða Á) bendli. Sá fyrsti er næst bendlinum.
vinstri = deque()
haegri = deque()

# --- Hermun á innslætti ---
# Förum í gegnum allar aðgerðirnar í inntaksstrengnum.
# Concept 1: Time Complexity - Lykkjan keyrir O(N) sinnum. Hver aðgerð innan
# lykkjunnar tekur O(1) tíma þökk sé deque. Heildarflækja O(N).
for char in s:
    if char == 'L':
        # Færa bendil til vinstri:
        # Taka síðasta staf úr vinstri hlutanum og setja fremst í hægri hlutann.
        if vinstri: # Athuga hvort vinstri sé tómur (tryggt af verkefni en gott samt)
            haegri.appendleft(vinstri.pop())
            
    elif char == 'R':
        # Færa bendil til hægri:
        # Taka fremsta staf úr hægri hlutanum og setja aftast í vinstri hlutann.
        if haegri: # Athuga hvort hægri sé tómur (tryggt af verkefni en gott samt)
            vinstri.append(haegri.popleft())
            
    elif char == 'B':
        # Bakktakki (Backspace):
        # Fjarlægja síðasta stafinn úr vinstri hlutanum (stafinn fyrir aftan bendil).
        if vinstri: # Athuga hvort vinstri sé tómur (tryggt af verkefni en gott samt)
            vinstri.pop()
            
    else:
        # Venjulegur stafur/tala:
        # Bæta stafnum við þar sem bendillinn er (sem er endinn á vinstri hlutanum).
        vinstri.append(char)

# --- Samsetning og úttak ---
# Sameinum vinstri og hægri hlutann til að fá lokastrenginn.
# join() tekur O(L) þar sem L er lengd hlutans. Heild O(N_final).
final_string = "".join(vinstri) + "".join(haegri)
print(final_string)

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Heildartímaflækja er O(N) vegna stakrar yfirferðar yfir inntaksstrenginn
# og O(1) aðgerða fyrir hvern staf með deque. Samsetning í lokin er O(N_final).
# Þetta er nógu skilvirkt fyrir N = 1,000,000.
# Aðaláhersla á Concept 2: Core Data Structures (Deque/Stack/List) fyrir skilvirka hermun.