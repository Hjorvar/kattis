import sys
from collections import defaultdict

# Aðgerðir fyrir hraðari innlestur
def input():
    return sys.stdin.readline().strip()

def input_int():
    return int(input())

def input_int_list():
    return list(map(int, input().split()))

# --- Innlestur Uppskrifta ---
# Lesum fjölda uppskrifta og kvittana
u, k = input_int_list()

# Concept 2: Geymum uppskriftir í dict fyrir hraða uppflettingu O(1) avg.
uppskriftir = defaultdict(dict) 
# Tímaflækja innlesturs: O(U + H_total)
for _ in range(u):
    nafn_rettar = input()
    fjoldi_hraefna_h = input_int()
    innihald_rettar = {}
    for _ in range(fjoldi_hraefna_h):
        line_parts = input().split()
        nafn_hraefnis = line_parts[0]
        magn_x = int(line_parts[1]) 
        innihald_rettar[nafn_hraefnis] = magn_x
    uppskriftir[nafn_rettar] = innihald_rettar

# --- Hagræðing: Söfnum heildarsölu hvers réttar ---
# Concept 2: Notum dict til að telja heildarsölu.
heildarsala_retta = defaultdict(int)
# Tímaflækja: O(K + N_total), þar sem N_total er heildarfjöldi rétta á öllum kvittunum.
for _ in range(k):
    fjoldi_retta_n = input_int()
    for _ in range(fjoldi_retta_n):
        line_parts = input().split()
        seldur_rettur = line_parts[0]
        magn_y = int(line_parts[1])
        # Leggjum við heildarsölu fyrir þennan rétt (O(1) avg.)
        heildarsala_retta[seldur_rettur] += magn_y

# --- Útreikningur á heildar hráefnisþörf ---
# Concept 2: Notum dict til að safna heildarmagni hráefna.
heildar_hraefni = defaultdict(int)
# Nú förum við bara yfir einstaka selda rétti (U_sold)
# Tímaflækja: O(U_sold * h_avg), þar sem U_sold <= U og U_sold <= N_total
for rettur, heildar_magn_y in heildarsala_retta.items():
    # Sækjum uppskriftina (O(1) avg.)
    innihald = uppskriftir[rettur]
    # Förum yfir hráefnin í þessari einu uppskrift
    for hraefni, magn_per_skammt in innihald.items():
        # Reiknum heildarþörf fyrir þetta hráefni frá þessum rétti
        # og leggjum við heildarsummuna (O(1) avg.)
        heildar_hraefni[hraefni] += magn_per_skammt * heildar_magn_y

# --- Úttak ---
# Concept 3: Sorting Algorithms
# Sækjum öll hráefnisnöfnin.
hraefnis_nofn = list(heildar_hraefni.keys())
# Röðum þeim. Tímaflækja: O(I log I).
hraefnis_nofn.sort()

# Prentum út niðurstöðuna. Tímaflækja: O(I).
for hraefni in hraefnis_nofn:
    magn = heildar_hraefni[hraefni]
    if magn > 0:
        print(f"{hraefni} {magn}")

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Ný nálgun: O(U+H_total) + O(K+N_total) + O(U_sold*h_avg) + O(I log I)
# Þetta ætti að vera hraðara en O(U+H_total) + O(K + N_total*h_avg) + O(I log I)
# þegar N_total er mikið stærra en U_sold (margir eins réttir seldir).