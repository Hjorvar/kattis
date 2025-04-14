import sys

def input():
    return sys.stdin.readline().strip()

# --- Nótnastaðall & Þáttun ---
# Concept 2: Map/Dict notað fyrir grunngildi nótna
note_base_values = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

# Fall til að þátta nótnastreng og skila staðlaðri MIDI tölu.
# Sér um Reglu 2 (Enharmonic Equivalence) með því að skila sama gildi fyrir tóna sem hljóma eins.
# Concept 18: String Processing (Parsing, Canonicalization via MIDI)
def parse_note_to_midi(note_str):
    if note_str == '-':
        return None # Sérstakt gildi fyrir þögn

    note_len = len(note_str)
    # Lágmarksathugun á formatti
    if note_len < 2: return None 

    note_name = note_str[0].upper()
    # Concept 2: Map/Dict lookup
    if note_name not in note_base_values: return None 

    # Finnum áttund (síðasti stafur)
    try:
        octave = int(note_str[-1])
    except ValueError:
        return None 

    # Finnum formerki (#/b) ef til staðar
    accidental = 0
    if note_len > 2 and note_str[1] in ('#', 'b'):
        if note_str[1] == '#':
            accidental = 1
        else: # note_str[1] == 'b'
            accidental = -1
    # Gætum bætt við villutékki ef lengd > 2 en stafur 1 er ekki formerki
    elif note_len > 2:
         return None

    # Reiknum MIDI gildi sem staðlað form fyrir nótuna
    try:
        base_val = note_base_values[note_name]
        # Formúla sem gefur rétt MIDI gildi (t.d. C4=60)
        midi_value = 12 * (octave + 1) + base_val + accidental
        return midi_value
    except KeyError: 
        return None 

# --- Aðalkóði ---
def main():
    n = int(input())
    melody1_str = input().split()
    melody2_str = input().split()

    # Trivial tilfelli
    if n == 0:
        print("Jebb")
        sys.exit()
        
    # Concept 2: Lists til að geyma staðlaðar MIDI raðir
    # Þáttun beggja laglína. Tímaflækja: O(N)
    midi_list1 = [parse_note_to_midi(note) for note in melody1_str]
    midi_list2 = [parse_note_to_midi(note) for note in melody2_str]

    # --- Samanburður á Laglínum ---
    # Concept 18: String Algorithms (Sequence Comparison)
    
    first_note_idx = -1 # Index fyrstu nótu (ekki þagnar)
    offset = 0          # Hliðrun milli laglína (í hálftónum)
    compatible = True   # Flagg til að segja hvort þær passi saman

    # Lykkja til að bera saman laglínurnar skref fyrir skref.
    # Tímaflækja: O(N)
    for i in range(n):
        note1 = midi_list1[i]
        note2 = midi_list2[i]

        is_pause1 = (note1 is None)
        is_pause2 = (note2 is None)

        # Skilyrði 1: Þagnir verða að vera á sömu stöðum
        if is_pause1 != is_pause2:
            compatible = False
            break # Óþarfi að halda áfram
            
        # Ef báðar eru nótur (ekki þagnir)
        if not is_pause1: 
            # Ef þetta er fyrsta nótan sem við finnum
            if first_note_idx == -1:
                first_note_idx = i
                # Reiknum hliðrunina (offset) - sér um Reglur 1, 3 og 4 saman
                offset = note2 - note1
            else:
                # Athugum hvort hliðrunin sé sú sama og fyrir fyrstu nótuna
                if note1 + offset != note2:
                    compatible = False # Hliðrunin breyttist, lögin eru ekki eins skv. reglum
                    break # Óþarfi að halda áfram

    # --- Úttak ---
    if compatible:
        print("Jebb")
    else:
        print("Neibb")

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Þáttun tekur O(N). Samanburður tekur O(N).
# Heildartímaflækja er O(N), sem er nógu hratt.

if __name__ == '__main__':
    main()