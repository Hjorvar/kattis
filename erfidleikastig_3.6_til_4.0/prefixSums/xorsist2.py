import sys

# Fall til að lesa heiltölu
def input_int():
    return int(sys.stdin.readline()) # strip() óþarfi með int()

# Fall til að lesa tvær heiltölur aðskildar með bili
def input_int_pair():
    return map(int, sys.stdin.readline().split())

# --- Fall til að reikna XOR Prefix Summu ---
# Concept 21: Bit Manipulation / Concept 11: Number Theory (Patterns)
# Reiknar 1 ^ 2 ^ ... ^ k á O(1) tíma með því að nota mynstur
# sem byggir á k mod 4.
def calculate_xor_prefix(k):
    # Ef k < 0 (getur gerst fyrir a-1 ef a=0, þó a>=1 hér), skilum 0
    if k < 0:
        return 0
        
    mod = k % 4
    if mod == 0:
        return k
    elif mod == 1:
        return 1
    elif mod == 2:
        return k + 1
    else: # mod == 3
        return 0

# --- Aðalkóði ---
# Lesum inn N
N = input_int()
# Lesum inn a og b
a, b = input_int_pair()

# Reiknum XOR summuna fyrir bilið [a, b]
# Concept 7: Prefix Sums (Hliðstæða með XOR)
# RangeXOR(a, b) = PrefixXOR(b) ^ PrefixXOR(a - 1)
# Tímaflækja: O(1) þar sem hvort fallkall tekur O(1).
xor_sum_b = calculate_xor_prefix(b)
xor_sum_a_minus_1 = calculate_xor_prefix(a - 1)
result = xor_sum_b ^ xor_sum_a_minus_1

# Athugum niðurstöðuna og prentum svar
# Tímaflækja: O(1)
if result == 0:
    print("Enginn")
elif 1 <= result <= N:
    print(result)
else: # result > N
    print("Gunnar")

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Öll aðalkóðaskrefin (innlestur, útreikningur, prentun) taka O(1) tíma.
# Heildartímaflækjan er O(1), sem er eins hratt og mögulegt er og stenst
# allar takmarkanir, jafnvel fyrir N=10^18.