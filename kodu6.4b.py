# Euromüntide seerias on kuus erineva nimiväärtusega senti: 1 sent, 2 senti, 5 senti, 10 senti, 20 senti, 50 senti. Sendid väärtustega 1, 2 ja 5 on pronksikarva (vasega kaetud teras), sendid väärtustega 10, 20 ja 50 on kullakarva (vasesulam, mis sisaldab alumiiniumi, tsinki ja tina, nn Nordic Gold).
# Peres on kombeks, et pronksikarva mündid panna hoiupõrsasse.
# Müntide andmed on failis kirjas nii, et iga mündi väärtus on eraldi real. Näiteks nii:
# 1
# 20
# 20
# 5
# 50
# 2
# 2
# 1
# Koostada funktsioon pronksikarva_summa, mis
# võtab argumendiks täisarvude järjendi ja
# tagastab selles järjendis olevate arvude 1, 2 ja 5 summa.
# Koostada programm, mis
# küsib kasutajalt selle faili nime, milles asuvad sentide väärtused;
# moodustab täisarvujärjendi vastavast failist loetud väärtustest;
# rakendab funktsiooni pronksikarva_summa, andes argumendiks koostatud täisarvujärjendi;
# väljastab ekraanile tulemuseks saadud kõikide pronksikarva sentide summa.

def pronksikarva_summa(fail):
    järjend = []
    for i in fail:
        järjend.append(int(i))
    
    j = 0
    summa = 0
    
    while j < len(järjend):
        if järjend[j] == 5 or järjend[j] == 2 or järjend[j] == 1:
            summa += järjend[j]
        j += 1
    return summa

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

print("Hoiupõrsasse läheb " + str(pronksikarva_summa(fail)) + " senti.")