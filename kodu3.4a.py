# On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Üks teine lillepood on otsustanud, et nende sünnipäeval saab iga klient kingituseks lilli nii, et esimene ostja saab ühe lille, teine ostja saab kolm lille, kolmas ostja saab viis lille, neljas ostja seitse lille jne.
# Koostada programm, mis
# küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil lillede koguarvu, mida pood klientidele kingib;
# väljastab kingitavate lillede koguarvu.

ostjad = int(input("Sisesta ostjate arv: "))

klient = 1
lill = 1
summa = 0

while klient <= ostjad:
    summa += lill
    lill += 2
    klient += 1
    
print("Lillede koguarv on " + str(summa) + ".")
