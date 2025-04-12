import sys

# --- Inntakslestur ---
try:
    n = int(sys.stdin.readline())
    # Höndlum N=0 ef það gæti gerst (þó N>=1 skv. lýsingu)
    if n == 0:
        print(0)
        exit()
    # Lesa kostnaðarlistann a
    a = list(map(int, sys.stdin.readline().split()))
    if len(a) != n:
        exit() # Villa ef lengd passar ekki
except Exception:
    exit() # Villa við lestur/umbreytingu

# --- Dýnamísk Forritun (DP) með minni-hagræðingu ---
# Atriði 12: Dynamic Programming

# Ef aðeins eitt verkefni er, þá er lágmarkskostnaður 0 (við getum sleppt því).
# DP útreikningurinn hér fyrir neðan höndlar þetta rétt.
if n == 1:
     # Kostnaður a[0] ef við gerum það, kostnaður 0 ef við sleppum. Lágmark 0.
     # En við verðum að velja *annað hvort*. Nei, við viljum lágmarka.
     # Lágmarkið er min(kostn_ef_gera, kostn_ef_sleppa).
     # Ef við gerum: a[0]. Ef við sleppum: 0.
     # Svo min(a[0], 0)? Nei, það virkar ekki ef a[0] er 0.
     # DP virkar: prev_do=a[0], prev_skip=0. Loop keyrir ekki. min(a[0], 0).
     # Þetta virðist rétt - lágmarkið er 0 ef a[0]>0, annars a[0].
     # Sem sagt: print(0) ef a[0]>0, print(a[0]) ef a[0]==0. Þetta er = min(a[0], 0).
     # Svo DP meðhöndlar N=1. Við fjarlægjum sér meðhöndlun.
     pass


# Grunntilfelli fyrir fyrsta verkefnið (index 0)
# Lágmarkskostnaður EF við gerðum verkefni 0
prev_do = a[0]
# Lágmarkskostnaður EF við slepptum verkefni 0
prev_skip = 0

# Atriði 1: Time Complexity - Lykkjan keyrir N-1 sinnum -> O(N) heildartími
# Ítreka fyrir verkefni 1 upp í N-1
for i in range(1, n):
    # Reikna lágmarkskostnað ef við GERUM verkefni i:
    # Kostnaður a[i] + lágmarkskostnaðurinn fram að i-1 (sama hvort i-1 var gert eða sleppt)
    curr_do = a[i] + min(prev_do, prev_skip)

    # Reikna lágmarkskostnað ef við SLEPPUM verkefni i:
    # Kostnaður 0 fyrir verkefni i + kostnaðurinn fram að i-1,
    # en AÐEINS ef verkefni i-1 var GERT.
    curr_skip = prev_do

    # Uppfæra 'fyrri' gildi fyrir næstu ítrun
    prev_do = curr_do
    prev_skip = curr_skip

# --- Lokasvar ---
# Eftir að hafa farið í gegnum öll verkefni, þá er heildarlágmarkskostnaðurinn
# sá minni af tveimur möguleikum fyrir síðasta verkefnið (N-1):
# annað hvort gerðum við það (prev_do) eða slepptum því (prev_skip).
final_min_cost = min(prev_do, prev_skip)

print(final_min_cost)

# --- Endir kóða ---