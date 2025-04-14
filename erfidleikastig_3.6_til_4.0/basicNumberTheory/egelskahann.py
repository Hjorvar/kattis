import sys

# Fall til að lesa heiltölu
def input_int():
    # Nota readline fyrir mögulega örlítið meiri hraða, strip() fjarlægir aukabil/línuskil
    return int(sys.stdin.readline().strip()) 

# --- Aðalkóði ---

# Lesum inn N
N = input_int()

# Lausnin byggir á formúlu fyrir Josephus vandamálið J(n, 2) þar sem
# annar hver er fjarlægður. Sú formúla er J(n, 2) = 2*L + 1,
# þar sem n = 2^m + L og 2^m er stærsta veldi af 2 <= n.

# Concept 11: Number Theory / Concept 21: Bit Manipulation
# Finnum stærsta veldi af 2, p = 2^m, sem er minna en eða jafnt og N.
# Notum bit_length() sem gefur fjölda bita sem þarf til að tákna N.
# Staða mikilvægasta bitsins (MSB) er þá bit_length() - 1.
# p = 2^(MSB_staða) = 1 << (MSB_staða).
# Tímaflækja: bit_length() og bit shift eru mjög hraðvirk, oft O(1) eða O(log N).
if N == 0: # Þó N>=1 sé gefið, gott að hafa til öryggis
    p = 0
elif N == 1: # bit_length(1)=1, 1<<(1-1) = 1<<0 = 1
    p = 1 << (N.bit_length() - 1)
else:
    # Ef N er veldi af 2 (t.d. 8), þá er N.bit_length() = m+1.
    # Við viljum p = N = 2^m. Stærsta veldi af 2 <= N.
    # Ef N er veldi af 2, þá er p = N.
    # Ef N er ekki veldi af 2, þá er p = 1 << (N.bit_length() - 1).
    # Þetta er hægt að gera með því að finna næsta veldi af 2 >= N og deila með 2,
    # eða nota þessa aðferð:
    power_of_2 = 1
    while power_of_2 * 2 <= N:
        power_of_2 *= 2
    p = power_of_2
    # Einfaldari leið með bit_length:
    # p = 1 << (N.bit_length() - 1) 
    
# Reiknum L = N - p
# Tímaflækja: O(1)
L = N - p

# Reiknum lokaniðurstöðuna J(n, 2) = 2*L + 1
# Tímaflækja: O(1)
result = 2 * L + 1

# Prentum svarið
print(result)

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Að finna stærsta veldi af 2 tekur í mesta lagi O(log N) tíma (með while lykkju)
# eða O(1)/O(log N) (með bit_length). Aðrir útreikningar eru O(1).
# Heildartímaflækja er því mjög lítil og stenst örugglega öll tímamörk.