import sys

# Fall til að lesa heiltölu
def input_int():
    return int(sys.stdin.readline().strip())

# --- Innlestur ---
n = input_int()
y = [] # Listi til að geyma tekjur
# Concept 2: Arrays/Lists - Notað til að geyma inntaksgögn
for _ in range(n):
    y.append(input_int())

# --- Röðun ---
# Concept 3: Sorting Algorithms - Röðun er lykillinn að skilvirkum útreikningi
# Tímaflækja: O(N log N)
y.sort()

# --- Útreikningur á Gini stuðli ---

# Reiknum teljarann með O(N) formúlu eftir röðun
# Formúla: Numerator = 2 * Sum_{k=0..n-1} y[k] * (2*k - n + 1)
# Concept 7: Prefix Sums (Hugmyndaleg tenging við útleiðslu formúlu)
# Tímaflækja: O(N) fyrir lykkjuna
numerator_sum_term = 0
for k in range(n):
    numerator_sum_term += y[k] * (2*k - n + 1)

numerator = 2 * numerator_sum_term

# Reiknum nefnarann
# Tímaflækja: O(N) fyrir sum()
total_sum = sum(y) 
# Tímaflækja: O(1)
# Ath: n > 0 og y_i > 0 tryggir total_sum > 0 og denominator != 0
denominator = 2 * n * total_sum 

# Reiknum Gini stuðulinn (passa flotöludeilingu)
# Tímaflækja: O(1)
if denominator == 0:
    # Þetta ætti ekki að gerast skv. skilyrðum (n>=1, y_i>0)
    # Ef n=1, þá er k=0, num_sum=y[0]*(0-1+1)=0, num=0. Den=2*1*y[0]. Gini=0.
    # Ef allir eru með sömu tekjur: y[k]=C. Sum y[k]*(2k-n+1) = C*Sum(2k-n+1) = C* [2*Sum(k) - n*(n-1+1)]
    # = C * [2*n*(n-1)/2 - n^2] = C * [n(n-1) - n^2] = C * [n^2-n-n^2] = -C*n.
    # Þetta virðist rangt. Athugum formúluna aftur.
    # Sum |yi-yj| = 2 * Sum_{i<j} (yj-yi) þegar raðað.
    # Sum_{k=0..n-1} y[k] * (k - (n-1-k)) = Sum y[k] * (2k - n + 1)
    # Já, formúlan ætti að vera rétt. Hún gefur 0 ef allir y_k eru eins:
    # Ef allir y_k = C: Num = 2 * C * Sum(2k-n+1) = 2 * C * [2*n(n-1)/2 - n(n-1)]? Nei, Sum(k)=n(n-1)/2. Sum(n-1)=n(n-1). Sum(1)=n.
    # Sum(2k - n + 1) = 2*Sum(k) - Sum(n) + Sum(1) ??? Ekki alveg.
    # Sum_{k=0..n-1} (2k - n + 1) = 2 * (n(n-1)/2) - n*(n-1) + 1*n = n(n-1) - n(n-1) + n = n. 
    # Þetta er RANGT. Summa k frá 0 til n-1 er n(n-1)/2.
    # Summa (n-1) frá 0 til n-1 er n*(n-1).
    # Summa (2k-n+1) = 2*n*(n-1)/2 - n*(n-1) = n(n-1) - n(n-1) = 0. JÁ!
    # Þannig að ef allir y_k eru eins (C), þá er numerator_sum_term = Sum C * (2k-n+1) = C * Sum(2k-n+1) = C * 0 = 0.
    # Teljarinn verður 0, Gini verður 0. Formúlan virkar!
    
    # Ef n=1, k=0. term = y[0]*(0-1+1)=0. num=0. den=2*1*y[0]. Gini=0. Rétt.
    gini = 0.0
else:
    gini = numerator / denominator

# --- Úttak ---
# Prentum Gini stuðulinn með nægri nákvæmni
# Notum format til að stýra úttaki
print(f"{gini:.17f}") # Prentum með mörgum aukastöfum til öryggis

# --- Samantekt Tímaflækju ---
# Concept 1: Time Complexity & Big O
# Röðun tekur O(N log N).
# Útreikningar á teljara og nefnara taka O(N).
# Heildartímaflækja ræðst af röðuninni: O(N log N).
# Þetta er nógu hratt fyrir N=10^5.