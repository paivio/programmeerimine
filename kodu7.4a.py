# Faili igal real on märk + (tuleb) või ? (ei tea veel) ja inimese nimi. Tehke see fail ise mingi tekstiredaktoriga (võib ka Thonnyga). Faili kodeeringuks kasutage UTF-8.
# Peo eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja programmi, mis arvutab
# maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale) ja
# minimaalse eelarve (arvestades, et kohale tulevad ainult need, kes on juba seda teatanud).
# Programmi loomisel on mõistlik aluseks võtta ülesande 6.3 lahendus, sh funktsioon eelarve, mis võtab argumendiks külaliste arvu ning arvutab ja tagastab eelarve (10 euro iga külalise jaoks ja 55 eurot ruumi rendiks). Programm
# küsib kasutajalt failinime;
# loeb sellest failist informatsiooni külaliste kohta;
# arvutab ja väljastab ekraanile kutsutud inimeste arvu;
# arvutab ja väljastab ekraanile inimeste arvu, kes on juba tulemisest teatanud;
# arvutab ja väljastab ekraanile maksimaalse eelarve, kasutades koostatud funktsiooni eelarve;
# arvutab ja väljastab ekraanile minimaalse eelarve, kasutades koostatud funktsiooni eelarve.

failinimi = input("Sisesta failinimi: ")
fail = open(failinimi, encoding="UTF-8")

jah = 0
vb = 0

ridades = fail.readlines()

for rida in ridades:
    if rida[0] == "+":
        jah += 1
    else:
        vb += 1
        
fail.close()

def eelarve(inimesi):
    summa = 55 + 10 * inimesi
    return summa
    
kutsutud = jah + vb
tuleb = jah

print("Maksimaalne eelarve: " + str((eelarve(kutsutud))) + " eurot")
print("Minimaalne eelarve: " + str((eelarve(tuleb))) + " eurot")
