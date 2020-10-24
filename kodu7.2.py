# Kirjutada programm, mis
# küsib kasutaja käest ühe sissekande (võib eeldada, et sissekanne on ilma reavahetusteta);
# kirjutab (UTF-8 kodeeringus) faili paevik.txt lõppu kolm rida:
# esimesel real praegune kuupäev ja kellaaeg sellisel kujul, nagu seda tagastab funktsioon datetime.today() (vt näidet);
# teisel real kasutaja sisestatud kirje;
# tühi rida (pole kohustuslik).

from datetime import datetime
lause = input("Sisesta sissekande tekst: ")

esimene_rida = str(datetime.today()) + "\n"
teine_rida =  str(lause) + "\n"
kolmas_rida = "\n"

fail = open("paevik.txt", "a", encoding="UTF-8")
fail.write(esimene_rida)
fail.write(teine_rida)
fail.write(kolmas_rida)

fail.close()