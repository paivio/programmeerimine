# Ada tahab minna reisile ja uurib viimase hetke pakkumisi. Võimalikud sihtkohad on kirjas failis (iga sihtkoht on eraldi real). Faili võite salvestada siit või koostada ise mõne tekstiredaktoriga.
# Koostada programm, mis
# küsib kasutajalt failinime (kasutaja sisestab failinime koos laiendiga, nt sihtkohad.txt);
# loeb sisestatud nimega failist andmed;
# näitab kõik sihtkohad koos järjekorranumbritega (alates 1);
# küsib kasutajalt, mitmes sihtkoht broneerida (kasutaja sisestab alati täisarvu);
# väljastab ekraanile vastavalt valitud arvule sihtkoha. 

failinimi = input("Palun sisestage faili nimi: ")
fail = open(failinimi, encoding="UTF-8")

i = 0
nimekiri = []

for rida in fail:
    i += 1
    print(str(i) + ". " + rida)
    nimekiri.append(rida)
    
koht_nr = int(input("Valige mitmes sihtkoht broneerida: "))
koht = nimekiri[koht_nr - 1]

print("Reis on broneeritud. Sihtkoht on " + koht)
    