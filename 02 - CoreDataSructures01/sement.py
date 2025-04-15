import sys

# Fall til að lesa tvær heiltölur
def input_int_pair():
    return map(int, sys.stdin.readline().split())

# Fall til að lesa eina heiltölu
def input_int():
    return int(sys.stdin.readline()) # strip() óþarfi með int()

# Lesum inn N og K
N, K = input_int_pair()

# --- Lausn með Orðabók (Hash Map) - O(N) meðaltímaflækja ---
# Concept 2: Core Data Structures (Map/Dict)
# Við notum orðabók til að geyma stærðir poka sem við erum búin að sjá.
# Þetta gerir okkur kleift að athuga á O(1) meðaltíma hvort poki með
# stærðina sem okkur vantar ("complement") hafi sést áður.
seen_sizes = {} 

found = False # Breytum til að vita hvort par fannst

# Förum yfir alla N pokana
# Concept 1: Time Complexity - Lykkjan keyrir O(N) sinnum.
for _ in range(N):
    # Lesum stærð núverandi poka
    current_size = input_int()
    
    # Reiknum út hvaða stærð við þurfum á hinum pokanum
    complement = K - current_size
    
    # Athugum hvort við höfum séð poka með stærðina 'complement' áður
    # Uppfletting í orðabók er O(1) að meðaltali.
    if complement in seen_sizes:
        # Við fundum par! Prentum stærðirnar og hættum.
        print(f"{complement} {current_size}")
        found = True
        break # Hættum leit um leið og par finnst
    
    # Ef við fundum ekki par, skráum að við höfum séð þennan poka
    # svo hann geti mögulega myndað par með poka sem kemur seinna.
    # Innsetning í orðabók er O(1) að meðaltali.
    seen_sizes[current_size] = True # Gildið skiptir ekki máli, bara lykillinn

# Ef lykkjan kláraðist án þess að finna par
if not found:
    print("Neibb")

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Lausnin fer einu sinni yfir listann af pokum (O(N)).
# Aðgerðirnar innan lykkjunnar (útreikningur, uppfletting/innsetning í dict)
# eru O(1) að meðaltali.
# Heildartímaflækja er því O(N) að meðaltali.
# Plássflækja er O(N) í versta falli fyrir orðabókina.
# Þetta er nógu skilvirkt fyrir gefnar takmarkanir.