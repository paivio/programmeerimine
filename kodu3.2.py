# On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Lillepoel on sünnipäev ja pood otsustas klientidele kinkida lilli nii, et päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab kolm lille, neljas ei saa midagi, viies ostja saab viis lille jne.
# Koostada programm, mis
# küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil lillede koguarvu, mida pood kingib;
# väljastab saadud lillede arvu ekraanile.

ostjad = int(input("Sisesta ostjate arv: "))

lill = 1
summa = 0

while lill <= ostjad:
    summa += lill
    lill += 2
    
print("Lillede koguarv on " + str(summa) + ".")
