# Järgnevatele funktsioonidele antakse argumendiks 5 x 5 tabel, milles iga element on kas täisarv lõigust 1 - 75 või täht X.
# Täht X sümboliseerib seda, et vastav arv on juba loositud.
# 1. Koostada funktsioon nurkademänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud mänguväli võidaks nurkademängu.
# 2. Koostada funktsioon diagonaalidemänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud mänguväli võidaks diagonaalidemängu.
# 3. Koostada funktsioon täismänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud mänguväli võidaks täismängu.

def nurkademänguks_vaja(tabel):
    nurgad = []
    nurgad_vaja = []
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if ((i == 0 or i == len(tabel)-1) and (j == 0 or j == len(tabel[i])-1)):
                nurgad.append(tabel[i][j])
    for n in range(len(nurgad)):
        if nurgad[n] != "X":
            nurgad_vaja.append(nurgad[n])
    return nurgad_vaja


def diagonaalidemänguks_vaja(tabel):
    diagonaalid = []
    diagonaalid_vaja = []
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if (i == j or i == len(tabel)-1-j):
                diagonaalid.append(tabel[i][j])
    for d in range(len(diagonaalid)):
        if diagonaalid[d] != "X":
            diagonaalid_vaja.append(diagonaalid[d])
    return diagonaalid_vaja


def täismänguks_vaja(tabel):
    täismäng_vaja = []
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if tabel[i][j] != "X":
                täismäng_vaja.append(tabel[i][j])
    return täismäng_vaja


tabel = ([ 2,  "X", 39, "X", "X"],
         ["X", "X", 38, "X", 64],
         ["X", 22, "X", 53,  74],
         ["X", 27, 31,  46,  62],
         ["X", "X", "X", "X", 1])

print(nurkademänguks_vaja(tabel))
print(diagonaalidemänguks_vaja(tabel))
print(täismänguks_vaja(tabel))