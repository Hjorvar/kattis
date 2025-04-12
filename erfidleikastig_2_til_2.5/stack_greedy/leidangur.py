# Flytjum inn nauðsynlegar einingar
# deque: Gagnagrind sem getur virkað sem skilvirkur hlaði (stack) eða biðröð (queue).
# Counter: Þægileg leið til að telja stök í safni (hér: telja hluti í bakpoka í lokin).
from collections import deque, Counter

# Lesum inn strenginn sem lýsir leiðangrinum
leiðangur = input()

# Búum til tóman deque sem mun virka sem bakpokinn/hlaðinn (stack).
# Hlaði notar LIFO (Last-In, First-Out) meginregluna.
# Við notum append() til að setja efst (eins og push)
# og pop() til að taka efsta (eins og pop).
bakpokkur = deque() 

# Breytum sem heldur utan um hvort leiðangurinn mistókst.
mistókst = False

# Orðabók til að vita hvaða hlut hver vondur kall krefst.
krefst = {'P': 'p', 'G': 'g', 'O': 'o'}

# Förum í gegnum hvern atburð (reit) í leiðangrinum, frá vinstri til hægri.
for atburður in leiðangur:
    # Ef atburður er hlutur á jörðinni ('p', 'g', eða 'o')
    if atburður in 'pgo':
        # *** GRÁÐUG ÁKVÖRÐUN (GREEDY) ***
        # Við setjum hlutinn alltaf í bakpokann (efst á hlaðann).
        # Þetta er gráðugt því við tökum hlutinn strax, með von um að hann
        # nýtist síðar. Að taka hann upp gefur fleiri möguleika en að skilja hann eftir.
        # *** HLAÐA AÐGERÐ (STACK) ***
        # append() bætir við hægri enda deque, sem við notum sem 'toppinn' á hlaðanum.
        bakpokkur.append(atburður)
        
    # Ef atburður er vondur kall ('P', 'G', eða 'O')
    elif atburður in 'PGO':
        # Finnum út hvaða hlut þessi vondi kall vill fá.
        hlutur_sem_vantar = krefst[atburður]
        
        # *** ATHUGUN (VARÚÐ - Ekki hrein stack aðgerð) ***
        # Þessi lína athugar hvort hluturinn sé *einhvers staðar* í bakpokanum.
        # Hún brýtur í raun örlítið stack hugsunina (Óli á bara að ná efst),
        # en hún virkar sem flýtileið: ef hluturinn er alls ekki til,
        # þá þarf ekki að leita og hægt er að segja strax að þetta mistókst.
        # Hrein stack lausn myndi sleppa þessu og láta while lykkjuna sjá um leitina.
        if hlutur_sem_vantar not in bakpokkur:
            mistókst = True
            break # Förum úr aðallykkjunni, leiðangurinn er búinn.

        # *** HLAÐA AÐGERÐIR (STACK) & GRÁÐUG AFGREIÐSLA ***
        # Nú þurfum við að finna hlutinn efst á hlaðanum.
        # Ef hann er ekki efst, þurfum við að fjarlægja (poppa) hluti
        # þar til við finnum hann eða hlaðinn tæmist.
        # Þetta er gráðug afgreiðsla: við leysum kröfuna strax.
        hlutur_fundinn = False
        while bakpokkur: # Á meðan eitthvað er í bakpokanum (á hlaðanum)
            # *** HLAÐA AÐGERÐ (STACK) ***
            # pop() tekur efsta hlutinn af hlaðanum (hægri enda deque).
            efsti_hlutur = bakpokkur.pop()
            
            # Er þetta hluturinn sem vondi kallinn vildi?
            if efsti_hlutur == hlutur_sem_vantar:
                # Já, við fundum hann. Hann er nú tekinn úr bakpokanum (poppaður).
                hlutur_fundinn = True
                break # Hættum að leita/poppa, krafan er uppfyllt.
            # else:
                # Ef þetta var EKKI rétti hluturinn, þá er honum hent
                # (hann er poppaður en ekki settur aftur í). Þetta er gert sjálfkrafa
                # með því að halda áfram í while lykkjunni án þess að gera neitt meira
                # við 'efsti_hlutur'.
                
        # Eftir while lykkjuna, athugum við hvort hluturinn fannst.
        # Þetta er nauðsynlegt ef 'if ... not in ...' athugunin var fjarlægð,
        # eða ef hún fann hlut djúpt niðri sem var svo óaðgengilegur.
        if not hlutur_fundinn: 
            # Ef við fórum í gegnum (hluta af) hlaðanum og fundum ekki hlutinn,
            # þá mistókst leiðangurinn.
            mistókst = True
            break # Förum úr aðallykkjunni.

    # Ef mistókst breytan var sett í True í einhverri af if/elif blokkunum,
    # hættum þá strax að vinna úr leiðangrinum.
    if mistókst:
        break

# Eftir að hafa farið í gegnum allan leiðangurinn (eða hætt fyrr vegna villu)
# Athugum hvort leiðangurinn mistókst.
if mistókst:
    print("Neibb")
else:
    # Ef leiðangurinn tókst, teljum við hversu mikið er eftir af hverri tegund
    # í bakpokanum (á hlaðanum).
    # *** HLAÐINN Í LOKIN (STACK) ***
    # Það sem er eftir í 'bakpokkur' deque er lokastaða hlaðans.
    fjöldi = Counter(bakpokkur)
    # Prentum út fjölda fyrir hverja tegund, 0 ef enginn er eftir.
    print(fjöldi.get('p', 0))
    print(fjöldi.get('g', 0))
    print(fjöldi.get('o', 0))

