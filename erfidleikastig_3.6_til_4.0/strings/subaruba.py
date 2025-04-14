import sys

# Aðgerðir fyrir innlestur
def input():
    return sys.stdin.readline().strip() # Fjarlægjum endingarlínuskil

def main():
    # Lesum aðgerð ('D' eða 'A')
    op_type = input()
    # Lesum fjölda lína
    n = int(input())
    
    # --- Undirbúningur ---
    # Concept 2: Set - Skilgreinum mengi af sérhljóðum.
    # MIKILVÆGT: Bætum 'y' við samkvæmt sýnidæmum!
    vowels = set('aeiouy') 

    # --- Vinnsla lína ---
    # Förum í gegnum hverja af n línunum
    for _ in range(n):
        line = input() # Lesum næstu textalínu
        # Concept 2: List - Notum lista til að byggja upp úttaksstrenginn skilvirkt
        result_chars = [] 
        
        # --- Dulkóðun ---
        if op_type == 'D':
            # Concept 18: String Processing (Iteration, Character Classification)
            # Förum staf fyrir staf í línunni
            for char in line:
                # Athugum hvort stafurinn (í lágstaf) sé sérhljóði
                if char.lower() in vowels:
                    # Ef já, bætum við lágstöfunum "ub" og svo stafnum sjálfum
                    # (til að varðveita upphaflegan há/lágstaf)
                    result_chars.append("ub" + char)
                else:
                    # Ef nei, bætum bara stafnum við
                    result_chars.append(char)

        # --- Afkóðun ---
        elif op_type == 'A':
            # Concept 18: String Processing (Iteration with index, Substring Check)
            i = 0 # Notum index til að geta hoppað yfir stafi
            line_len = len(line)
            while i < line_len:
                # Athugum hvort við höfum 'u', 'b', og a.m.k. einn staf eftir OG
                # fyrstu tveir séu "ub" (óháð há/lágstaf) OG sá þriðji sé sérhljóði
                # Nota slicing s[i:i+2] til að forðast index villu ef i+1 er síðasti stafur.
                if i + 2 < line_len and \
                   line[i:i+2].lower() == "ub" and \
                   line[i+2].lower() in vowels:
                    # Ef allt passar, þá er þetta dulkóðunar "ub".
                    # Við bætum aðeins sérhljóðanum við útkomuna
                    result_chars.append(line[i+2])
                    # Hoppum yfir alla þrjá stafina ('u', 'b', sérhljóði)
                    i += 3
                else:
                    # Ef mynstrið passar ekki, bætum núverandi staf við 
                    # og förum áfram um einn staf.
                    result_chars.append(line[i])
                    i += 1
        
        # --- Úttak fyrir línuna ---
        # Sameinum stafina í listanum í einn streng og prentum
        # Tímaflækja join: O(L_line)
        print("".join(result_chars))

# Keyrum aðalfallið
if __name__ == '__main__':
    main()

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Heildartímaflækja er O(L), þar sem L er heildarlengd textans.
# Þetta næst með því að fara bara einu sinni yfir hvern staf og nota 
# skilvirkar O(1) aðgerðir (uppfletting í mengi, viðbót við lista).
# Aðaláhersla á Concept 18 (String Processing) og Concept 2 (Set/List).