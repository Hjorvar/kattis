import sys

# Módúllinn sem nota skal
MOD = 1000000007

# --- Inntakslestur ---
try:
    n_str = sys.stdin.readline()
    if not n_str:
        raise ValueError("Tóm inntakslína")
    n = int(n_str.strip()) # Fjöldi goðsagna
except Exception as e:
    # print(f"Input Error reading N: {e}", file=sys.stderr)
    exit()

# --- Útreikningur ---

# Jaðartilfelli: Ef n < 20, ómögulegt að velja 20 ólíkar.
if n < 20:
    print(0)
else:
    # Atriði 20: Combinatorics (Umraðanir og Samsetningar)
    # Skref 1: Reikna fjölda umraðana P(n, 20) módúló MOD.
    # Þetta telur leiðir til að úthluta 20 ólíkum goðsögnum í 20 aðgreind skref,
    # þar sem röðin milli skrefa skiptir máli.
    perm_n_20 = 1
    for i in range(20):
        term = n - i
        perm_n_20 = (perm_n_20 * term) % MOD

    # Skref 2: Leiðrétta fyrir óröðuðu pörin.
    # Það eru 3 skref í ferlinu þar sem lið velur 2 goðsagnir samtímis
    # (Skref 8: Rautt velur 2, Skref 9: Blátt velur 2, Skref 16: Blátt velur 2).
    # Fyrir þessi skref skiptir innbyrðis röð valanna ekki máli (A svo B = B svo A).
    # Útreikningurinn P(n, 20) telur þetta sem ólíka möguleika (oftelur um 2).
    # Þar sem þetta gerist 3 sinnum, höfum við oftalið um þáttinn 2*2*2 = 8.
    # Við þurfum því að deila niðurstöðunni perm_n_20 með 8.

    # Deiling í módúló reikningi er margföldun með módúló umhverfu.
    # Atriði 19: Advanced Number Theory (Modular Multiplicative Inverse)
    # Notum litlu setningu Fermats til að finna umhverfu 8 (þar sem MOD er prímtala):
    # inv(8) = 8^(MOD-2) % MOD
    inv8 = pow(8, MOD - 2, MOD)

    # Deilum með 8 með því að margfalda með umhverfunni.
    final_result = (perm_n_20 * inv8) % MOD

    # --- Úttak ---
    # Atriði 1: Time Complexity - Ennþá mjög hratt, O(log MOD) vegna pow, eða O(1) ef við lítum á 20 sem fasta.
    print(final_result)

# --- Endir kóða ---