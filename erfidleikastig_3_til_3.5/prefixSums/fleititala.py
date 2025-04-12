import sys
import math

# Lesa inntak
d_str = sys.stdin.readline()
k_str = sys.stdin.readline()

d = int(d_str)
# k getur verið mjög stórt, Python meðhöndlar stórar heiltölur sjálfkrafa
k = int(k_str)

# Meðhöndla jaðartilfellið d=0
if d == 0:
    print(f"{0.0:.10f}")
else:
    # Atriði 1: Time Complexity & Big O
    # Bein ítrun O(k) skrefa er of hæg ef k er stórt (t.d. 10^18).
    # Við notum því nálgun fyrir stórt k.

    # Stærðfræðileg innsýn (tengist Atriði 7 - Summation):
    # Samtals = d * (1 + 1/2 + ... + 1/(2^k)) = d * (2 - 1/(2^k))

    # Meðhöndlun á stóru k og fljótandi kommutölum:
    # Fyrir nægilega stórt k (t.d. k > 100), verður 1/(2^k) hverfandi lítið
    # miðað við áskilda nákvæmni (10^-5). Í slíkum tilfellum er
    # samtals ≈ d * (2 - 0) = 2 * d.
    # Við veljum viðmiðunarmörk (threshold) fyrir k. 100 er öruggt val.
    k_threshold = 100

    if k >= k_threshold:
        # O(1) nálgun fyrir stórt k. Notum float fyrir útreikninginn.
        result = 2.0 * float(d)
    else:
        # Fyrir lítið k (k < 100) er ítrun nógu hröð og nákvæm.
        # Þetta forðast líka útreikning á mjög háum veldum af 2 beint.
        # Þessi hluti tekur O(k) tíma, en þar sem k < 100 er það í lagi.
        total_distance = float(d) # Byrjum með upphafskastið
        current_term = float(d)   # Núverandi vegalengd (fyrir næsta skopp)

        # Lykkja fyrir k skopp
        for _ in range(k):
            current_term /= 2.0      # Helminga vegalengdina
            total_distance += current_term # Bæta við heildarvegalengd

        result = total_distance

    # Skila niðurstöðu með nægjanlegri nákvæmni.
    # f-string með .10f tryggir að minnsta kosti 10 aukastafi.
    print(f"{result:.10f}")