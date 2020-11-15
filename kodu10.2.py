# Kirjutada programm, mis küsib kasutajalt failinime, loeb vastava nimega failist täidetud Sudoku tabeli ning kontrollib, kas see on
# korrektne Sudoku lahendus. Kui lahendus on korrektne, väljastada "OK" ja kui lahendus on mittekorrektne, siis väljastada "Viga",
# millele võib järgneda info vea asukoha kohta.

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
sudoku = []

for i in fail:
    read_laiali = i.split()
    rida = []
    for j in read_laiali:
        rida.append(int(j))
    sudoku.append(rida)

fail.close()


def kastid_korras(maatriks):
     for rea_nurk in range(0, 9, 3):
         for veeru_nurk in range(0, 9, 3):
             kast = []
             for i in range(3):
                 for j in range(3):
                     kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
             if sorted(kast) != list(range(1, 10)):
                 return False
     return True
 
 
def read_korras(maatriks):
    for i in range(len(maatriks)):
        rida = []
        for j in range(len(maatriks[i])):
            rida.append(maatriks[i][j])
    if sorted(rida) != list(range(1, 10)):
         return False
    return True


def veerud_korras(maatriks):
    for j in range(len(maatriks[0])):
        veerg = []
        for i in range(len(maatriks)):
            veerg.append(maatriks[i][j])
        if sorted(veerg) != list(range(1, 10)):
            return False
    return True


if kastid_korras(sudoku) is True and read_korras(sudoku) is True and veerud_korras(sudoku) is True: 
    print("OK")
else:
    print("Viga")         