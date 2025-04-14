import sys
import math # Þurfum sqrt eða isqrt

# Aðgerð til að lesa heiltölu
def input_int():
    # Nota readline fyrir mögulega örlítið meiri hraða, strip() fjarlægir aukabil/línuskil
    return int(sys.stdin.readline().strip()) 

# Lesum inn radíus r
r = input_int()

# Heildarfjöldi punkta sem uppfylla skilyrðið
total_points = 0

# Reiknum r^2 einu sinni til að nota ítrekað
# Python sér sjálfkrafa um stórar heiltölur (allt að 10^12 hér)
r_squared = r * r

# --- O(r) lausn: Ítrun yfir x ---
# Concept 1: Time Complexity - Þessi lykkja keyrir 2r+1 sinnum, sem er O(r).
# Þetta er nógu hratt fyrir r allt að 10^6.
for x in range(-r, r + 1):
    # Fyrir fast x, finnum hversu stórt y^2 má vera: y^2 <= r^2 - x^2
    y_limit_squared = r_squared - x*x
    
    # Ef r^2 - x^2 er neikvætt (sem gerist bara ef |x| > r, en lykkjan okkar nær bara að |x|=r),
    # þá eru engin rauntölulausn fyrir y, og því engin heiltölulausn.
    # En þar sem við notum sqrt á það hér á eftir, þá þurfum við að passa að taka ekki sqrt af neikvæðri tölu.
    # Hins vegar ætti y_limit_squared aldrei að vera neikvætt innan range(-r, r+1).
    # Þegar x = r eða x = -r, þá er y_limit_squared = 0.
    
    # Concept 25: Geometry / Concept 11: Number Theory
    # Finnum stærsta mögulega |y| þannig að y^2 <= y_limit_squared.
    # Þetta er floor(sqrt(y_limit_squared)).
    # Notum int() til að fá heiltöluhlutann, eða math.isqrt fyrir betri nákvæmni/hraða.
    # Þar sem y_limit_squared >= 0, þá er þetta öruggt.
    ymax = int(math.sqrt(y_limit_squared)) 
    # Eða: ymax = math.isqrt(y_limit_squared) # Ef Python 3.8+
    
    # Fyrir þetta fasta x, þá gilda allar heiltölur y frá -ymax til +ymax.
    # Fjöldi þeirra er 2 * ymax + 1.
    # (t.d. ef ymax=2, þá eru gildin -2, -1, 0, 1, 2, sem eru 2*2+1 = 5 talsins)
    points_for_this_x = 2 * ymax + 1
    
    # Bætum þessum fjölda við heildarsummuna.
    total_points += points_for_this_x

# Prentum heildarfjöldann
print(total_points)

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Lykkjan keyrir O(r) sinnum.
# Aðgerðir innan lykkju (reikningur, sqrt/isqrt) taka í mesta lagi O(log r) eða O(1) (fer eftir útfærslu á sqrt).
# Heildartímaflækja er því O(r) eða O(r log r), sem er nógu hratt fyrir r=10^6.