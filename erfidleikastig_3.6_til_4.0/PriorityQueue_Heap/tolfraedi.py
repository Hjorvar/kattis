import sys
import heapq # Innbyggt hrúgu reiknirit
from collections import defaultdict # Orðabók sem gefur sjálfgefið gildi

# Aðgerðir fyrir (mögulega) hraðari innlestur
def input():
    return sys.stdin.readline().strip()

def main():
    # Lesum fjölda aðgerða
    Q = int(input())

    # --- Gagnagrindur ---
    # Concept 2: Map/Dict - Höldum utan um fjölda hvers aldurs
    counts = defaultdict(int) 
    
    # Concept 9: Priority Queue / Heap - Tvær hrúgur fyrir min/max
    min_heap = [] # Hefðbundin lágmarkshrúga
    max_heap = [] # Virkar sem hámarkshrúga með því að geyma neikvæð gildi
    
    # Höldum utan um heildarsummu og fjölda fyrir meðaltal
    total_sum = 0
    total_count = 0

    # --- Vinnsla aðgerða ---
    # Concept 1: Time Complexity - Lykkjan keyrir Q sinnum.
    # Aðgerðir innan lykkju taka O(log U) amortized (U=fjöldi einstakra aldra).
    for _ in range(Q):
        line = input().split()
        op = line[0]
        # Aldur getur verið stór, Python sér um stórar heiltölur
        x = int(line[1]) 

        if op == 'A':
            # --- Bæta við aldri ---
            # Ef þetta er í fyrsta skipti sem við sjáum þennan aldur
            if counts[x] == 0:
                # Bætum við í báðar hrúgurnar
                # Concept 9: Heap push - O(log U)
                heapq.heappush(min_heap, x)
                heapq.heappush(max_heap, -x) # Setjum neikvætt gildi fyrir max-heap
            
            # Uppfærum teljara og summu
            counts[x] += 1
            total_sum += x
            total_count += 1

        elif op == 'R':
            # --- Fjarlægja aldur ---
            # Athugum hvort aldurinn sé til (tryggt skv. lýsingu)
            if counts[x] > 0:
                # Lækkum teljara og summu
                counts[x] -= 1
                total_sum -= x
                total_count -= 1
                # ATH: Fjarlægjum EKKI úr hrúgunum strax (Lazy Deletion)
            
        # --- Úttak eftir aðgerð ---
        if total_count == 0:
            # Ef enginn er eftir í hirðinni
            print("-1 -1 -1")
        else:
            # Finnum raunverulegt lágmark með Lazy Deletion
            # Á meðan efsta stakið í min_heap er með fjölda 0 í counts...
            # Concept 9: Heap pop (implicit remove) - Amortized O(log U)
            while min_heap and counts[min_heap[0]] == 0:
                heapq.heappop(min_heap) 
            # Efsta stakið er núna raunverulegt lágmark
            current_min = min_heap[0]

            # Finnum raunverulegt hámark með Lazy Deletion
            # Á meðan efsta stakið í max_heap (sem er neikvætt) samsvarar
            # aldri sem er með fjölda 0 í counts...
            while max_heap and counts[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            # Efsta stakið (tekið sem jákvætt) er núna raunverulegt hámark
            current_max = -max_heap[0]

            # Reiknum meðaltal
            average_age = total_sum / total_count

            # Prentum niðurstöðu með umbeðinni nákvæmni
            # Notum f-string og format specifier fyrir nákvæmni
            print(f"{current_min} {current_max} {average_age:.6f}")

# Keyrum aðalfallið
if __name__ == '__main__':
    main()

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Heildartímaflækja er O(Q * log U), þar sem U <= Q er fjöldi einstakra aldra.
# Þetta er vegna O(log U) aðgerða hrúganna (heap) innan lykkju sem keyrir Q sinnum.
# Þetta er nógu skilvirkt fyrir Q = 100,000.
# Concept 24: Advanced Data Structures - Notkun á hrúgum á þennan hátt til að halda utan
# um min/max í breytilegu mengi telst oft til fullkomnari gagnagrinda/aðferða.