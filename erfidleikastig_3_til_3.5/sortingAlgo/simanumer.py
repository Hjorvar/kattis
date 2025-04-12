import sys
import bisect # Innifalið í Python, veitir föll fyrir tvíleit

# --- Inntakslestur ---
try:
    n = int(sys.stdin.readline())
    phone_numbers = []
    # Atriði 2: Core Data Structures - Lesum númerin í lista
    for _ in range(n):
        # Lesum símanúmer, fjarlægjum bil/línubil, bætum í lista
        phone_numbers.append(sys.stdin.readline().strip())

    q_count = int(sys.stdin.readline())
    queries = []
    for _ in range(q_count):
        # Lesum fyrirspurnir
        queries.append(sys.stdin.readline().strip())

except Exception as e:
    # print(f"Input Error: {e}", file=sys.stderr)
    exit() # Hætta ef villa við lestur

# --- Forvinnsla: Röðun ---
# Atriði 3: Sorting Algorithms - Röðum listanum strengjafræðilega
# Atriði 1: Time Complexity - Þetta tekur O(N*L*logN) þar sem L=7
phone_numbers.sort()

# --- Vinnsla fyrirspurna ---
# Atriði 1: Time Complexity - Lykkjan keyrir Q sinnum
for q in queries:
    # Atriði 5: Binary Search - Notum bisect til að finna rétt svið

    # Lengd fyrirspurnar
    l = len(q)
    # Ef fyrirspurn er lengri en 7 (gegn skilyrðum), svarið er 0
    if l > 7:
        print(0)
        continue

    # Finnum neðri mörk (lower bound):
    # Finnum indexinn á fyrsta númeri sem er >= q
    # bisect_left gefur þetta. Tekur O(L*logN)
    start_index = bisect.bisect_left(phone_numbers, q)

    # Finnum efri mörk (upper bound):
    # Við viljum finna indexinn á fyrsta númeri sem er > öllum númerum
    # sem byrja á q. Þetta er það sama og að finna indexinn *fyrir aftan*
    # síðasta númerið sem byrjar á q.
    # Við getum fundið þetta með því að finna efri mörk strengsins sem
    # er q fyllt upp í 7 stafi með hæsta mögulega staf ('9').
    q_max = q + '9'*(7-l)
    # bisect_right finnur innsetningarpunkt fyrir q_max *eftir* öllum
    # gildum sem eru jöfn q_max. Þetta gefur okkur réttan enda-index.
    # Tekur O(L*logN)
    end_index = bisect.bisect_right(phone_numbers, q_max)

    # Fjöldi númera sem byrja á q er mismunurinn á indexunum
    count = end_index - start_index

    # --- Úttak ---
    print(count)

# --- Endir kóða ---