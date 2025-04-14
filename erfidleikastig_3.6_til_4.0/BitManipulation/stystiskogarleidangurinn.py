import sys
import math
import itertools # Ekki notað í DP lausn

# Óendanlegt gildi fyrir fjarlægðir og DP töflu
INF = float('inf')

# Fall til að lesa heiltölur úr línu
def input_int_list():
    return list(map(int, sys.stdin.readline().split()))

# --- Aðalkóði ---
def main():
    # Lesum grunn upplýsingar
    n, m, s = input_int_list()
    # Lesum bardagatíma (0-indexað)
    x = input_int_list() 

    # --- Undirbúningur: Stysta leið milli allra skrímsla ---
    # Concept 16: Shortest Paths (All-Pairs Shortest Path)
    # Búum til fjarlægðarfylki fyrir ferðatíma
    # dist[i][j] = stysti ferðatími milli skrímslis i og j
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0 # Enginn ferðatími til sín sjálfs
        
    # Lesum inn beinar leiðir
    for _ in range(m):
        u, v, t = input_int_list()
        # Leiðréttum í 0-index
        u -= 1
        v -= 1
        # Geymum stystu beinu leiðina (ef margar eru á milli sömu)
        dist[u][v] = min(dist[u][v], t)
        dist[v][u] = min(dist[v][u], t) # Óstefndur graf

    # Keyrum Floyd-Warshall til að finna allar stystu leiðir
    # Tímaflækja: O(N^3) - Lítið mál fyrir N <= 16
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF: # Gætum að óendanlegu
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # --- TSP með Dýnamískri Forritun og Bitmöskum ---
    # Concept 12: Dynamic Programming / Concept 21: Bit Manipulation & Bitmask DP
    # dp[mask][last] = minnsti tími (ferða+bardaga) til að heimsækja skrímsli
    #                  í 'mask', enda á skrímsli 'last'.
    # Stærð dp töflu: (2^n) x n
    dp = [[INF] * n for _ in range(1 << n)]

    # Grunn tilfelli: Byrjum á skrímsli 1 (index 0). Tíminn er bardagatími þess.
    dp[1 << 0][0] = x[0] 

    # Ítrun yfir öll möguleg ástönd (maska og síðasta skrímsli)
    # Tímaflækja: O(2^N * N^2) - Höfuðverkurinn, en dugar fyrir N <= 16.
    for mask in range(1, 1 << n):
        for last in range(n):
            # Ef við höfum ekki náð þessu ástandi ennþá, eða 'last' er ekki í maskinu
            if not (mask & (1 << last)) or dp[mask][last] == INF:
                continue

            # Reynum að fara frá 'last' til 'next' (sem er ekki í maskinu)
            for next_node in range(n):
                if not (mask & (1 << next_node)): # Ef 'next' er ekki þegar heimsótt
                    # Nýr maski inniheldur 'next'
                    new_mask = mask | (1 << next_node)
                    # Nýr tími = gamli tími + ferðatími + bardagatími næsta skrímslis
                    # Ath: dist[last][next] gæti verið INF ef engin leið er á milli
                    if dist[last][next_node] != INF:
                       new_time = dp[mask][last] + dist[last][next_node] + x[next_node]
                       # Uppfærum dp töfluna ef þessi leið er styttri
                       dp[new_mask][next_node] = min(dp[new_mask][next_node], new_time)

    # --- Finnum lágmarkstíma (án tillits til ljósta) ---
    # Förum yfir öll lokaástönd (öll skrímsli heimsótt, enda á 'last')
    min_raw_time = INF
    final_mask = (1 << n) - 1
    for last in range(n):
        min_raw_time = min(min_raw_time, dp[final_mask][last])

    # --- Reiknum sparnað frá ljóstum ---
    # Concept 3: Sorting - Röðum til að finna stærstu tímana
    # Tímaflækja: O(N log N)
    sorted_x = sorted(x)
    
    savings = 0
    # Tökum summu af s stærstu gildunum (passa að fara ekki út fyrir mörk)
    # Tímaflækja: O(s) eða O(N)
    num_smites = min(s, n) # Getum ekki notað fleiri ljóstur en skrímsli eru til
    for i in range(num_smites):
        savings += sorted_x[n - 1 - i]
        
    # --- Lokaniðurstaða ---
    # Ef engin leið fannst sem heimsótti öll skrímsli (mjög ólíklegt ef graf er samanhangandi)
    if min_raw_time == INF:
         # Hér gæti þurft að meðhöndla ósamanhangandi graf, en lýsing gefur það ekki til kynna.
         # Skilum kannski stærstu mögulegu tölu eða villu. Gerum ráð fyrir að lausn finnist.
         final_time = 0 # Eða önnur meðhöndlun? Látum vera 0 ef INF.
    else:
         final_time = min_raw_time - savings

    # --- Úttak ---
    # Úttakið þarf að vera heiltala skv. lýsingu ("Skrifaðu út stysta tímann")
    # Þó millireikningar gætu orðið float ef við notuðum sqrt, þá eru allir tímar int.
    print(int(final_time)) # Breytum í int ef þörf krefur (ætti ekki að vera)

# Keyrum aðalfallið
if __name__ == '__main__':
    main()

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Floyd-Warshall: O(N^3)
# TSP DP: O(2^N * N^2)
# Röðun fyrir sparnað: O(N log N)
# Heildarflækja ræðst af TSP DP: O(N^3 + 2^N * N^2).
# Fyrir N=16 er 2^16*16^2 um 17 milljónir, N^3 er um 4000. Flækjan er innan marka.