# On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Lillepoel on sünnipäev ja pood otsustas klientidele kinkida lilli nii, et päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab kolm lille, neljas ei saa midagi, viies ostja saab viis lille jne.
# Koostada programm, mis
# küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
# arvutab for-tsükli ja funktsiooni range() abil lillede koguarvu, mida pood kingib;
# väljastab saadud lillede arvu ekraanile.

ostjad = int(input("Sisesta ostjate arv: "))

kokku = 0
for i in range(1, ostjad + 1, 2):
    kokku += i
    
print("Lillede koguarv on " + str(kokku))