# Kirjutada funktsioon on_legaalne_bingo_tabel, mis võtab argumendiks 5 x 5 tabeli, milles iga element on täisarv lõigust 1 - 75,
# ning tagastab tõeväärtuse vastavalt sellele, kas arvud on veergudesse jaotatud vastavalt Bingo reeglitele.
# Et tegu oleks legaalse Bingo Loto mänguväljaga, peavad vasakpoolseimas veerus olema arvud lõigust 1 - 15,
# järgmises veerus lõigust 16 - 30 ja nii edasi, kuni viimases veerus on arvud lõigust 61 - 75.
# Lihtsuse mõttes võib eeldada, et kõik arvud on unikaalsed ehk ükski arv ei esine antud tabelis rohkem kui üks kord.

def on_legaalne_bingo_tabel(tabel):
    B = []
    I = []
    N = []
    G = []
    O = []

    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if j == 0:
               B.append(tabel[i][j])
            elif j == 1:
                I.append(tabel[i][j])
            elif j == 2:
                N.append(tabel[i][j])
            elif j == 3:
                G.append(tabel[i][j])
            else:
                O.append(tabel[i][j])
    if max(B) < 16 and min(I) > 15 and max(I) < 31 and min(N) > 30 and max(N) < 46 and min(G) > 45 and max(G) < 61 and min(O) > 60 and max(O) < 76:
        on_legaalne = True
    else:
        on_legaalne = False
    return on_legaalne
    



tabel = ([1,30,34,55,75], [10,16,40,50,67], [5,20,38,48,61], [4,26,43,49,70], [15,17,33,51,66])
print(on_legaalne_bingo_tabel(tabel))