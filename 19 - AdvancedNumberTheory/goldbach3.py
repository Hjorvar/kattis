import sys

def input_int():
    return int(sys.stdin.readline())

# --- Miller-Rabin Frumtalnapróf ---
# Concept 11: Basic Number Theory (Primality Checking)
# Þetta fall notar Miller-Rabin reikniritið til að athuga á skilvirkan hátt
# hvort stór tala 'n' sé líklega frumtala. Fyrir valdar grunntölur ('a')
# er þetta próf ákvarðanandi (ekki bara líkindalegt) fyrir allar tölur
# upp að mjög hárri markatölu (mun hærri en 2*10^8).
# Concept 1: Time Complexity - Tímaflækjan er u.þ.b. O(k * (log N)^3) þar sem k er
# fjöldi grunntalna, sem er mun hraðara en O(sqrt(N)) eða O(N log log N) fyrir stök próf.
def is_probably_prime(n):
    # Grunntilfelli og einfaldar athuganir
    if n < 2:
        return False
        
    # Athugum fyrst deilingu með litlum frumtölum - flýtir fyrir mörgum samsettum tölum.
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n == p:
            return True # Ef n er ein af litlu frumtölunum
        if n % p == 0:
            return False # Ef n er deilanlegt með lítilli frumtölu (og ekki sú frumtala sjálf)
            
    # --- Kjarni Miller-Rabin ---
    # Skrifum n - 1 sem d * 2^s þar sem d er oddatala.
    # Þetta er hluti af stærðfræðinni á bakvið prófið.
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
        
    # Prófum með vel völdum grunntölum ('a'). Þessar grunntölur tryggja
    # nákvæmni fyrir allar tölur upp að 2^64.
    # Hver grunntala 'a' virkar sem "vitni" (witness). Ef talan 'n' stenst
    # prófið fyrir öll þessi vitni er hún frumtala (innan þessara marka).
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        # Ef a er margfeldi af n, sleppum því (sjaldgæft)
        if a % n == 0:
            continue
            
        # Reiknum x = a^d mod n. Notum pow(a, d, n) fyrir skilvirkni.
        # Concept 19 (Advanced Number Theory) gæti nefnt modular exponentiation.
        x = pow(a, d, n)
        
        # Ef x er 1 eða n-1 (-1 mod n), þá gæti n verið frumtala. Halda áfram með næsta 'a'.
        if x == 1 or x == n - 1:
            continue
            
        # Annars, endurtökum í s-1 skipti: x = x^2 mod n
        # Ef við finnum x = n-1 á leiðinni, þá gæti n verið frumtala.
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break # Förum út úr innri lykkju og höldum áfram með næsta 'a'
        else:
            # Ef innri lykkjan kláraðist án þess að finna x = n-1,
            # þá er 'n' örugglega samsett tala fyrir þetta vitni 'a'.
            return False
            
    # Ef talan 'n' stóðst prófið fyrir öll vitnin 'a', þá er hún frumtala (með vissu innan 2^64).
    return True

# --- Lítið Sáld Eratoþenesar ---
# Concept 11: Basic Number Theory (Sieve of Eratosthenes)
# Notað hér sem forvinnsla/hagræðing til að fá lista af litlum frumtölum hratt.
# Keyrt bara upp að föstu lágmarki ('limit').
def get_small_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, isprime in enumerate(sieve) if isprime]

def main():
    N = input_int()
    
    # --- Tilfelli 1: Lausn á forminu 2 + 2 + P3 ---
    # Athugum P3 = N - 4 með Miller-Rabin.
    # Concept 11: Primality checking (using Miller-Rabin)
    if is_probably_prime(N - 4):
        print(f"2 2 {N - 4}")
        return
    
    # --- Tilfelli 2: Lausn á forminu 3 + P2 + P3 ---
    target = N - 3
    
    # Hagræðing: Nota lítið sáld til að fá lista af litlum frumtölum (< limit).
    # Concept 11: Sieve (limited use for optimization)
    limit = 100000 # Veljum mark fyrir "litlar" frumtölur
    small_primes = get_small_primes(limit)
    
    # Leit 1: Prófum fyrst með P2 úr listanum af litlum frumtölum.
    # Þetta flýtir fyrir ef önnur talnanna (P2 eða P3) er lítil.
    for p in small_primes:
        # Þurfum bara að leita upp að helmingnum af summunni
        if p > target // 2:
            break
        # Athugum hvort P3 = target - p sé frumtala með Miller-Rabin
        # Concept 11: Primality checking (using Miller-Rabin)
        if is_probably_prime(target - p):
            print(f"3 {p} {target - p}")
            return
            
    # Leit 2: Ef lausn fannst ekki, höldum áfram með stærri oddatölur P2.
    # Byrjum á næstu oddatölu eftir 'limit'.
    p = limit + 1 if (limit + 1) % 2 == 1 else limit + 2
    while p <= target // 2:
        # Athugum hvort BÆÐI p og target - p séu frumtölur með Miller-Rabin.
        # Concept 11: Primality checking (using Miller-Rabin) - tvö köll hér.
        if is_probably_prime(p) and is_probably_prime(target - p):
            print(f"3 {p} {target - p}")
            return
        # Förum í næstu oddatölu
        p += 2
        
    # Ef ekkert fannst (ætti ekki að gerast samkvæmt tilgátu).
    print("Neibb")

if __name__ == '__main__':
    main()