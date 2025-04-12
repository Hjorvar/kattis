import sys

# Aðgerð til að lesa eina línu frá staðalinntaki
def input():
    return sys.stdin.readline().strip()

# Set (mengi) sem geymir alla leyfilega sérhljóða í lokin.
# Að athuga hvort stak sé í mengi (set lookup) tekur að meðaltali O(1) tíma.
serhljodar = {'a', 'e', 'i', 'o', 'u', 'y'}

# Lesum inn strenginn frá notanda
s = input()
# Finnum lengd strengsins, n. Þetta tekur O(1) tíma.
n = len(s)

# Flöggum breytu til að vita hvort strengurinn uppfylli skilyrðin
er_desiigner = True

# --- Tímaflækjuathuganir (Time Complexity Checks) ---
# Allar athuganir hér að neðan miða að því að skila 'False' (og þar með "Neibb") eins fljótt
# og hægt er ef strengurinn uppfyllir EKKI skilyrðin.

# Skilyrði 1: Lengd verður að vera að minnsta kosti 4 ('b' + 'rr' + sérhljóði)
# Þessi athugun tekur O(1) tíma.
if n < 4:
    er_desiigner = False
else:
    # Skilyrði 2: Fyrsti stafurinn verður að vera 'b'.
    # Að nálgast s[0] tekur O(1) tíma. Samanburðurinn tekur O(1) tíma.
    if s[0] != 'b':
        er_desiigner = False
    
    # Skilyrði 3: Síðasti stafurinn verður að vera sérhljóði.
    # Að nálgast s[n-1] (eða s[-1]) tekur O(1) tíma.
    # Athugun í 'serhljodar' menginu tekur O(1) tíma að meðaltali.
    elif s[-1] not in serhljodar:
        er_desiigner = False
    
    # Skilyrði 4: Allir stafir á milli þess fyrsta og síðasta verða að vera 'r'.
    # Við þurfum að ítra frá index 1 upp í (en ekki með) n-1.
    # Þessi lykkja keyrir í mesta lagi n-2 sinnum.
    # Innan lykkjunnar er O(1) aðgerð (nálgast s[i] og bera saman við 'r').
    # Í versta falli (ef allir stafir eru 'r') tekur þessi hluti O(N) tíma,
    # þar sem N er lengd strengsins. Ef stafur sem er ekki 'r' finnst fyrr,
    # hættir lykkjan fyrr.
    # Þetta er tímafrekasti hluti kóðans og ræður heildartímaflækjunni.
    else: 
        for i in range(1, n - 1):
            if s[i] != 'r':
                er_desiigner = False
                break # Hættum í lykkjunni um leið og við finnum staf sem er ekki 'r'

# --- Úttak ---
# Heildartímaflækja kóðans er O(N) vegna lykkjunnar í Skilyrði 4.
# Allar aðrar aðgerðir taka O(1) tíma.
if er_desiigner:
    print("Jebb")
else:
    print("Neibb")