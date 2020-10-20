# Korvpalluri vabavisete senist visketabavust saab (teatud mööndustega) kasutada tuleviku visete tõenäosusena.
# Koostada programm, mis
# küsib kasutajalt visketabavuse (tabavustõenäosuse) protsentides (täisarv 0 kuni 100);
# simuleerib while-tsükli abil 1000 viset ja igal viskel (arvestades tõenäosust) väljastab, kas see tabas;
# iga viske kohta peab väljastama ühe rea ja see rida peab sisaldama sõna tabas või mööda
# arvutab kokku tabanud visete arvu ja see väljastab selle kõige viimasena.

from random import randint

tabavus = int(input("Sisestage visketabavuse protsent: "))

i = 1
j = 0

while i <= 1000:
    if randint(1, 100) <= tabavus:
        print(str(i) + ". vise tabas")
        i += 1
        j += 1
    else:
        print(str(i) + ". vise mööda")
        i += 1
print("Tabas " + str(j) + " viset.")