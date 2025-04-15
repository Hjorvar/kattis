import sys
import math
import itertools # Fyrir permutations

# --- Fjarlægðarfall ---
# Concept 25: Geometry - Evklíðsk fjarlægð
def distance(p1, p2):
    # hypot(dx, dy) reiknar sqrt(dx*dx + dy*dy)
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# --- Innlestur ---
def input():
    return sys.stdin.readline().strip()

def main():
    N = int(input())
    
    # Geymum staðsetningar. points[0] er vöruhús (0,0).
    # Concept 2: Arrays/Lists
    points = [(0.0, 0.0)] # Nota kommutölur strax til öryggis
    all_x_zero = True
    for _ in range(N):
        x, y = map(int, input().split())
        if x != 0:
            all_x_zero = False
        points.append((float(x), float(y)))

    # --- Sérlausnir fyrir einföld tilfelli ---
    
    # Ef engir pakkar eru
    if N == 0:
        print(f"{0.0:.10f}") 
        return
        
    # Ef aðeins einn pakki
    if N == 1:
        # Leið: 0 -> 1 -> 0
        dist = distance(points[0], points[1]) * 2.0
        print(f"{dist:.10f}")
        return
        
    # Ef allir punktar eru á Y-ás (x=0)
    # Concept 1: Time Complexity - O(N) lausn fyrir þetta sértilfelli
    if all_x_zero:
        min_y = 0.0
        max_y = 0.0
        # Finnum lægsta og hæsta y-hnit (miðað við 0)
        for i in range(1, N + 1):
            min_y = min(min_y, points[i][1])
            max_y = max(max_y, points[i][1])
        # Stysta leiðin er 0 -> max_y -> min_y -> 0
        # Heildarvegalengd = max_y + (max_y - min_y) + abs(min_y)
        # Einfaldast í 2 * (max_y - min_y)
        dist = 2.0 * (max_y - min_y)
        print(f"{dist:.10f}")
        return

    # --- Almenn lausn: TSP fyrir lítið N (N <= 8) ---
    # Notum Brute-Force með umröðunum (permutations).
    # Concept 20: Combinatorics (Permutations)
    # Concept 1: Time Complexity - O(N! * N), dugar fyrir N <= 8 (og líklega N<=10)
    
    min_total_distance = float('inf')
    
    # Búum til lista yfir indexa afhendingarstaða (1 til N)
    delivery_indices = list(range(1, N + 1))
    
    # Ítrum í gegnum allar mögulegar raðir (N! stykki)
    for perm in itertools.permutations(delivery_indices):
        current_distance = 0.0
        last_point_index = 0 # Byrjum í vöruhúsi (index 0)
        
        # Reiknum vegalengdina fyrir þessa röð
        # Concept 13: Graph Theory - Lengd hringferðar
        for current_point_index in perm:
            # Vegalengd frá síðasta punkti að núverandi
            current_distance += distance(points[last_point_index], points[current_point_index])
            last_point_index = current_point_index
            
        # Bætum við vegalengd frá síðasta afhendingarstað aftur í vöruhús
        current_distance += distance(points[last_point_index], points[0])
        
        # Uppfærum lágmarksvegalengd ef þessi leið er styttri
        min_total_distance = min(min_total_distance, current_distance)
        
    # Prentum bestu vegalengdina sem fannst með nægri nákvæmni
    print(f"{min_total_distance:.10f}")

    # ATH: Fyrir aðeins stærra N (t.d. 10-18) væri DP lausnin (Held-Karp) betri.
    # Concept 12: Dynamic Programming / Concept 21: Bitmask DP - O(2^N * N^2)

if __name__ == '__main__':
    main()