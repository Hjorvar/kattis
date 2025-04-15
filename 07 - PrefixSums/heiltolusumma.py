# Lesum inn heiltöluna N
n = int(input())

# Reiknum summuna
summa = 0

# Concept 1: Time Complexity & Big O -> Skiptum í tilfelli til að nota O(1) formúlu.
if n >= 1:
    # Tilfelli 1: N er jákvætt (eða 1)
    # Concept 7: Prefix Sums (Formula) -> Notum Gauss formúluna beint.
    # Formúlan S = n*(n+1)/2 gefur summuna 1 + 2 + ... + n.
    # Notum heiltöludeilingu (//) þar sem útkoman er alltaf heiltala.
    # Tímaflækja: O(1)
    summa = n * (n + 1) // 2
else:
    # Tilfelli 2: N er núll eða neikvætt
    # Við þurfum summuna N + (N+1) + ... + 0 + 1.
    # Þetta er summa neikvæðu talnanna (-|N|*(|N|+1)/2) plús summan af 0 og 1 (sem er 1).
    # |N| er -n þegar n <= 0.
    # Tímaflækja: O(1)
    abs_n = -n 
    summa_negative_part = -(abs_n * (abs_n + 1) // 2)
    summa = summa_negative_part + 1 # Bætum við 0 + 1

# Prentum út niðurstöðuna
# Tímaflækja: O(1) (prentun á einni tölu)
print(summa)

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Lausnin notar enga lykkju sem fer í gegnum N tölur.
# Hún notar aðeins nokkrar einfaldar stærðfræðiaðgerðir sem taka fastan tíma.
# Heildartímaflækjan er því O(1), sem er mjög skilvirkt og stenst allar takmarkanir.