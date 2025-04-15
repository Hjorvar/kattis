import sys
from collections import deque # Fyrir BFS biðröð

# Aðgerðir fyrir innlestur
def input():
    return sys.stdin.readline().strip()

def input_int():
    return int(input())

def input_int_list():
    return list(map(int, input().split()))

# Fall til að reikna fjarlægð í öðru veldi (til að forðast sqrt og nota heiltölur)
def distance_sq(p1, p2):
    # p1 og p2 eru túplur/listar (x, y, z)
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    # Mikilvægt að reikningurinn passi í 64-bita tölu ef hnit eru stór
    # Python sér um þetta sjálfkrafa.
    return dx*dx + dy*dy + dz*dz

# --- Innlestur ---
N = input_int()
ships = [] # Listi til að geyma skipagögn: [(x, y, z, r), ...]
for i in range(N):
    ships.append(input_int_list())

M = input_int()
bombs = [] # Listi til að geyma sprengjugögn: [(x, y, z, r), ...]
for i in range(M):
    bombs.append(input_int_list())

# --- Grafsmíði fyrir keðjuverkun ---
# Concept 13: Basic Graph Theory - Búum til aðlægnilista (adjacency list)
# adj[i] mun innihalda lista af indexum skipa sem skip 'i' sprengir ef það springur.
# Tímaflækja: O(N^2)
adj = [[] for _ in range(N)]
for i in range(N):
    xi, yi, zi, ri = ships[i]
    exploding_radius_i = 2 * ri # Radíus sprengingar frá skipi i
    
    for j in range(N):
        if i == j: continue # Skip sprengir ekki sjálft sig beint

        xj, yj, zj, rj = ships[j]
        
        # Reiknum fjarlægð milli miðja skipa i og j (í öðru veldi)
        # Concept 25: Geometry - 3D fjarlægð
        dist_ij_sq = distance_sq((xi, yi, zi), (xj, yj, zj))
        
        # Reiknum mörkin fyrir snertingu/skörun (í öðru veldi)
        threshold_sq = (exploding_radius_i + rj) ** 2
        
        # Ef sprenging frá skipi i nær skipi j
        if dist_ij_sq <= threshold_sq:
            adj[i].append(j) # Bætum við stefndum legg i -> j

# --- Upphafseyðilegging og BFS uppsetning ---
# Concept 2: Core Data Structures - Boolean listi og Deque
destroyed = [False] * N # Hvaða skip eru eyðilögð?
queue = deque()         # Biðröð fyrir BFS

# Athugum hvaða skip verða fyrir beinum áhrifum af upphaflegu sprengjunum
# Tímaflækja: O(N * M)
for i in range(N):
    if destroyed[i]: continue # Ef þegar eyðilagt, sleppa

    xi, yi, zi, ri = ships[i]
    for k in range(M):
        xk, yk, zk, rk = bombs[k]
        
        dist_ik_sq = distance_sq((xi, yi, zi), (xk, yk, zk))
        threshold_sq = (ri + rk) ** 2
        
        if dist_ik_sq <= threshold_sq:
            # Skip i er eyðilagt af sprengju k
            destroyed[i] = True
            queue.append(i) # Bæta við í biðröð fyrir BFS
            break # Engin þörf á að athuga fleiri sprengjur fyrir þetta skip

# --- Keðjuverkun (BFS) ---
# Concept 13: Basic Graph Theory (BFS) - Finnum alla næranlega hnúta
# Tímaflækja: O(N + E), þar sem E <= N^2. Heild O(N^2).
while queue:
    # Tökum næsta eyðilagða skip úr biðröðinni
    u = queue.popleft() 
    
    # Athugum hvaða önnur skip það sprengir
    for v in adj[u]:
        # Ef nágrannaskipið 'v' er ekki þegar eyðilagt
        if not destroyed[v]:
            destroyed[v] = True # Merkjum það eyðilagt
            queue.append(v)     # Bætum því í biðröðina

# --- Telja eftirlifendur ---
# Tímaflækja: O(N)
survivor_count = 0
for i in range(N):
    if not destroyed[i]:
        survivor_count += 1

# --- Úttak ---
print(survivor_count)

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Grafsmíði O(N^2) + Upphafseyðilegging O(N*M) + BFS O(N^2) + Talning O(N)
# Heildarflækjustig ræðst af O(N^2 + N*M).
# Fyrir N, M <= 1000 er þetta í mesta lagi í kringum 1-2 milljón aðgerðir, sem er vel innan marka.