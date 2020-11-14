# Kirjutada funktsioon juhuslik_bingo, mis ei võta ühtegi argumenti ja tagastab juhuslikult genereeritud korrektse Bingo Loto tabeli.
# Oma lahenduse kontrollimiseks võib kasutada ülesande Reeglite kontrollimine lahendusfunktsiooni.
# Oluline on tähele panna, et ükski arv ei tohi veerus (ega terves tabelis) korduda. Arvude genereerimiseks võib kasutada moodulist random funktsiooni sample. Komplekti arvudest esimese Bingo tabeli veeru jaoks saaks selle abil genereerida nii: sample(range(1, 16), 5).

from random import *

def juhuslik_bingo():
    bingo = []
    k = 0
    kordaja = 5

    while kordaja > 0:
        rida = sample(range(1+k, 16+k), 5)
        bingo.append(rida)
        k += 15
        kordaja -= 1
 
# python 3 transpose matrix
    for rida in bingo:
        uus_bingo = [[bingo[j][i] for j in range(len(bingo))] for i in range(len(bingo[0]))]
        
    return uus_bingo




print(juhuslik_bingo())