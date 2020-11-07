# Järgnevatele funktsioonidele antakse argumendiks 5 x 5 tabel, milles iga element on kas täisarv lõigust 1 - 75 või täht X. Täht X sümboliseerib seda, et vastav arv on juba loositud.
# 1. Koostada funktsioon võitis_nurkademängu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud nurkademängu.
# 2. Koostada funktsioon võitis_diagonaalidemängu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud diagonaalidemängu. Selleks koostada ja kasutada kahte abifunktsiooni:
# Funktsioon x_peadiagonaalil, mis tagastab antud tabeli peadiagonaalil olevate X arvu.
# Funktsioon x_kõrvaldiagonaalil, mis tagastab antud tabeli kõrvaldiagonaalil olevate X arvu.
# 3. Koostada funktsioon võitis_täismängu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud täismängu.

# Nurkademängu võidu kontroll:
def võitis_nurkademängu(tabel):
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if tabel[0][0] == "X" and tabel[0][4] == "X" and tabel[4][0] == "X" and tabel[4][4] == "X":
                nurgad_võit = True
            else:
                nurgad_võit = False
    return nurgad_võit


# Diagonaalidemängu võidu kontroll (peadiagonaalil olevate x-ide arv):
def x_peadiagonaalil(tabel):
    x_pea = 0
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if i == j:
                if tabel[i][j] == "X":
                    x_pea += 1
    return x_pea


# Diagonaalidemängu võidu kontroll (kõrvaldiagonaalil olevate x-ide arv):
def x_kõrvaldiagonaalil(tabel):
    x_kõrval = 0
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if (i + j) == 4:
                if tabel[i][j] == "X":
                    x_kõrval += 1
    return x_kõrval


# Diagonaalidemängu võidu kontroll:
def võitis_diagonaalidemängu(tabel):
    if x_peadiagonaalil(tabel) == 5 and x_kõrvaldiagonaalil(tabel) == 5:
        diag_võit = True
    else:
        diag_võit = False
    return diag_võit


# Täismängu võidu kontroll:
def võitis_täismängu(tabel):
    x_arv = 0
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if tabel[i][j] == "X":
                x_arv += 1
    if x_arv == 25:
        täis_võit = True
    else:
        täis_võit = False
    return täis_võit



tabel = ([2, 'X', 39, 'X', 61],
         ['X', 'X', 38, 'X', 64],
         ['X', 22, 'X', 53, 74],
         ['X', 27, 31, 46, 62],
         ['X', 27, 41, 56, 68])

print(võitis_nurkademängu(tabel))
print(võitis_diagonaalidemängu(tabel))
print(võitis_täismängu(tabel))
print(x_kõrvaldiagonaalil(tabel))
print(x_peadiagonaalil(tabel))