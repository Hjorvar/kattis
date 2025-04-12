import sys

# --- Inntakslestur ---
try:
    # Lesa alla línuna sem inniheldur ENF/DNF segðina sem streng
    dnf_expression = sys.stdin.readline().strip()
except Exception:
    exit() # Hætta ef lestur mistekst

# --- Vinnsla ---

# Atriði 18: String Algorithms (Strengjaþáttun - Parsing)
# Kjarni lausnarinnar er að þátta inntaksstrenginn rétt skv. ENF forminu.
# Þetta krefst grundvallar strengjaaðgerða.

# Nota split() til að skipta segðinni í einstakar klausur út frá " EDA ".
clauses = dnf_expression.split(" EDA ")

# Upphafsstöðva flagg sem segir til um hvort segðin sé fullnægjanleg
satisfiable = False

# Ítreka í gegnum strengjahlutana sem tákna klausur
for clause_str in clauses:
    # Atriði 18: String Algorithms (Vinnsla á klausustreng)
    # Hreinsa klausustrenginn: nota slicing til að fjarlægja '(' og ')'
    # og strip() til að fjarlægja bil.
    if len(clause_str) >= 2 and clause_str.startswith("(") and clause_str.endswith(")"):
        inner_clause = clause_str[1:-1].strip()
    else:
        inner_clause = clause_str.strip() # Ef engir svigar

    # Nota split() til að skipta klausunni í einstaka lýsingar (literals) út frá " OG ".
    literals = inner_clause.split(" OG ")

    # Atriði 2: Core Data Structures - Notum mengi (set) fyrir mótsagnaskoðun
    positive_vars = set()
    negative_vars = set()
    contains_contradiction = False

    # Ítreka í gegnum strengjahlutana sem tákna lýsingar
    for literal in literals:
        literal = literal.strip() # Hreinsa bil
        if not literal: continue # Sleppa tómum strengjum

        # Atriði 18: String Algorithms (Vinnsla á lýsingarstreng)
        # Nota startswith('!') til að athuga neitun.
        # Nota slicing til að ná í breytunafnið.
        is_negated = literal.startswith("!")
        var_name = literal[1:] if is_negated else literal

        # Athuga mótsögn með mengjunum
        if is_negated:
            if var_name in positive_vars:
                contains_contradiction = True
                break
            negative_vars.add(var_name)
        else:
            if var_name in negative_vars:
                contains_contradiction = True
                break
            positive_vars.add(var_name)

    # Ef engin mótsögn fannst í þessari klausu, þá er öll segðin fullnægjanleg
    if not contains_contradiction:
        satisfiable = True
        break # Hættum leit því við fundum sanna klausu

# --- Úttak ---
# Atriði 1: Time Complexity - Heildartíminn ræðst af lengd inntaksstrengsins O(L)
if satisfiable:
    print("Jebb")
else:
    print("Neibb")

# --- Endir kóða ---