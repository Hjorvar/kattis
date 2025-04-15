import sys
from collections import defaultdict # Einfaldar talningu

# Fall til að lesa tvær heiltölur
def input_int_pair():
    # Nota split() beint á readline(), map() breytir í int
    return map(int, sys.stdin.readline().split()) 

# Lesum inn fjölda nemenda
n = int(sys.stdin.readline()) 

# --- Tíðnitalning ---
# Concept 2: Core Data Structures (Map/Dict)
# Notum orðabók til að telja hversu oft hvert nemendanúmer kemur fyrir í pörunum.
# defaultdict(int) byrjar alla nýja teljara í 0.
counts = defaultdict(int)

# Fjöldi pára sem við lesum inn er n/2 + 1
num_pairs_to_read = n // 2 + 1 

# Lesum inn öll pörin og teljum tölurnar
# Tímaflækja: O(N/2 * 1) = O(N) fyrir lykkjuna og O(1) avg. fyrir dict aðgerðir.
for _ in range(num_pairs_to_read):
    a, b = input_int_pair()
    counts[a] += 1
    counts[b] += 1

# --- Finnum auka tölurnar ---
# Þær tölur sem koma nákvæmlega tvisvar fyrir eru tölurnar í auka parinu.
extra_numbers = []
# Förum í gegnum orðabókina. Tímaflækja: O(U) þar sem U <= N er fjöldi einstakra númera.
for num, count in counts.items():
    if count == 2:
        extra_numbers.append(num)
        # Við ættum að finna nákvæmlega tvær tölur
        if len(extra_numbers) == 2:
            break # Óþarfi að leita lengra

# --- Úttak ---
# Röðum tölunum tveimur þannig að sú minni komi á undan. O(1) þar sem listinn er bara 2 stök.
extra_numbers.sort() 

# Prentum út auka parið
print(f"{extra_numbers[0]} {extra_numbers[1]}")


# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Innlestur og talning tekur O(N) tíma að meðaltali.
# Að finna auka tölurnar tekur O(N) tíma í versta falli.
# Röðun á tveimur tölum og prentun tekur O(1).
# Heildartímaflækja er O(N), sem er nógu hratt fyrir N=200,000.