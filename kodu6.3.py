# Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad ja ülejäänute kohta ei ole midagi teada. Peo eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja programmi, mis arvutab
# maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale) ja
# minimaalse eelarve (arvestades, et kohale tulevad ainult need, kes on juba seda teatanud).
# Esmalt koostada funktsioon eelarve, mis võtab argumendiks külaliste arvu tähistava täisarvu ning arvutab ja tagastab selle põhjal eelarve kogusumma. Näiteks argumendiga 5 tagastab funktsioon arvu 105.
# Seejärel koostada programm, mis
# küsib kasutajalt kutsutud inimeste arvu;
# küsib kasutajalt inimeste arvu, kes on juba tulemisest teatanud;
# arvutab ja väljastab ekraanile maksimaalse eelarve, kasutades koostatud funktsiooni eelarve;
# arvutab ja väljastab ekraanile minimaalse eelarve, kasutades koostatud funktsiooni eelarve.

def eelarve(inimesi):
    summa = 55 + 10 * inimesi
    return summa
    
kutsutud = int(input("Mitu inimest on kutsutud: "))
tuleb = int(input("Mitu inimest tuleb: "))

print("Maksimaalne eelarve: " + str((eelarve(kutsutud))) + " eurot")
print("Minimaalne eelarve: " + str((eelarve(tuleb))) + " eurot")