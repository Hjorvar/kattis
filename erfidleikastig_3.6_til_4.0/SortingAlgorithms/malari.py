import sys

# Aðgerðir fyrir innlestur
def input():
    return sys.stdin.readline().strip()

def input_int_list():
    return list(map(int, input().split()))

# --- Innlestur ---
# Tímaflækja: O(1)
N, M = input_int_list()

# Tímaflækja: O(M) fyrir innlestur + smá overhead fyrir append
intervals = []
for _ in range(M):
    # Lesum hvert bil [i, j]
    i, j = input_int_list()
    # Concept 2: Core Data Structures (Arrays/Lists) - Geymum bilin í lista
    intervals.append([i, j])

# --- Röðun ---
# Concept 3: Sorting Algorithms
# Röðum bilunum eftir upphafspunkti (fyrra stakinu í hverju pari).
# Tímaflækja: O(M log M) - Þetta er oft tímafrekasti hluti lausnarinnar.
intervals.sort(key=lambda x: x[0])

# --- Sameining skaraðra bila ---
# Concept 8: Greedy Algorithms (implicit) - Förum í gegnum röðuð bil og sameinum gráðugt.
# Tímaflækja: O(M) þar sem við förum bara einu sinni yfir listann.
merged_intervals = []
for current_start, current_end in intervals:
    # Ef merged_intervals er tómur eða núverandi bil byrjar eftir að síðasta sameinaða bil endaði
    # Ath: Við notum merged_intervals[-1][1] + 1 til að sameina ekki bil sem bara snertast (t.d. [1,3] og [4,5])
    # Ef við VILJUM sameina snertandi bil notum við: current_start > merged_intervals[-1][1]
    # Samkvæmt lýsingu málar hann samfellt, svo við þurfum að athuga hvort upphafspunktur sé > endapunktur síðasta bils.
    if not merged_intervals or current_start > merged_intervals[-1][1]:
        # Þetta bil skarast ekki við fyrra sameinað bil, byrjum nýtt sameinað bil.
        merged_intervals.append([current_start, current_end])
    else:
        # Þetta bil skarast við síðasta sameinaða bil.
        # Lengjum síðasta sameinaða bil ef þetta bil nær lengra.
        merged_intervals[-1][1] = max(merged_intervals[-1][1], current_end)

# --- Reikna heildarlengd ---
# Tímaflækja: O(M) þar sem fjöldi sameinaðra bila er í mesta lagi M.
total_painted = 0
for start, end in merged_intervals:
    # Lengd bilsins er end - start + 1
    total_painted += (end - start + 1)

# --- Úttak ---
# Prentum heildarfjöldann. O(1).
print(total_painted)

# Berum saman við N/2. Notum heiltölur til að forðast flotöluvillur.
# Concept 1: Time Complexity - Allar þessar aðgerðir eru hraðar.
# Heildarflækjustig ræðst af röðuninni: O(M log M).
if total_painted * 2 > N:
    print("The Mexicans took our jobs! Sad!")
else:
    print("The Mexicans are Lazy! Sad!")