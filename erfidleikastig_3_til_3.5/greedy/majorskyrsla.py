import sys

# Lesa inntak
n, k = map(int, sys.stdin.readline().split())

# Atriði 7: Prefix Sums (og almenn stærðfræði)
# Við notum þekkingu á summuformúlum.
# Hámarksvísir fyrir fyrstu 'm' tölur (ef þeim er snúið við) er m*(m-1)/2.
# Finnum minnsta 'm' þannig að m*(m-1)/2 >= k.
# Atriði 1: Time Complexity - Þessi lykkja keyrir í mesta lagi O(sqrt(k)) eða O(n) sinnum.
m = 0
# Notum integer deilingu '//' til öryggis, þó margföldun sé líka í lagi hér.
while m * (m - 1) // 2 < k:
    m += 1
    # Öryggistékk, ætti ekki að gerast skv. takmörkunum á k.
    if m > n + 1:
         # Hér gæti komið villa ef k væri of stórt
         break

# Núverandi vísir ef við snúum við fyrstu 'm' tölunum.
current_k = m * (m - 1) // 2

# Reiknum mismuninn sem þarf að leiðrétta.
# Við höfum vísi 'current_k' en viljum 'k'. Við þurfum að lækka vísinn um 'diff'.
diff = current_k - k

# Atriði 8: Greedy Algorithms
# Græðgis skref 1: Búum til byrjunarlista með því að snúa við fyrstu 'm'
# tölunum og láta restina óhreyfða. Vísirinn er 'current_k'.
# P = [m, m-1, ..., 1, m+1, m+2, ..., n]

# Atriði 2: Core Data Structures - Notum lista í Python.
# Atriði 3: Sorting - Byggjum á raðaðri röð.
prefix_reversed = list(range(m, 0, -1))  # Tölur m niður í 1
suffix_sorted = list(range(m + 1, n + 1)) # Tölur m+1 upp í n
p = prefix_reversed + suffix_sorted

# Græðgis skref 2: Lækkum vísinn um 'diff' með einni víxlun.
# Til að lækka vísinn um 'diff' þurfum við að fjarlægja þann viðsnúning
# sem gaf 'diff' í vísinn. Þetta er viðsnúningurinn á milli
# 1-talinna staða 'diff' og 'diff+1'.
# Í 0-töldum lista eru þetta indexar 'diff-1' og 'diff'.
# Ef diff=0, þá var current_k == k og engin þörf á víxlun.
if diff > 0:
    # Ath: Staða 'diff' (1-talin) inniheldur töluna m-(diff-1) = m-diff+1
    # Staða 'diff+1' (1-talin) inniheldur töluna m-diff
    # Við víxlum þeim til að fjarlægja viðsnúninginn.
    # Indexarnir í 0-töldum lista eru diff-1 og diff.
    # Gætum þess að 'diff' sé innan marka formálans (diff <= m-1).
    # Þetta ætti alltaf að vera satt þar sem diff = m*(m-1)/2 - k >= 0.
    # Stærsta gildi diff er m*(m-1)/2 (þegar k=0). Minnsta gildi er 0.
    # Stærsta mögulega 1-talin staða í formálanum er m-1.
    # Þar sem diff <= m*(m-1)/2, þá er ekki víst að diff <= m-1 alltaf?
    # Jú, því viðsnúningurinn sem gefur 'diff' er alltaf til staðar.
    # Staða 1 gefur 1, staða 2 gefur 2... staða m-1 gefur m-1.
    # Við þurfum að fjarlægja framlagið 'diff'. Það kemur frá stöðu 'diff'.
    p[diff - 1], p[diff] = p[diff], p[diff - 1]


# Prenta út listann með bilum á milli talna.
print(*(p))