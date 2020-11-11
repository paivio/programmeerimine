### NB! NB! See ei ole lõplik versioon. Tulevad parandused!

# Arvutikontrolltöö nr 1 (variant 1).
# Päivi Ojala
# ÜL 2

# Impordin juhusliku arvu väljastamise:
from random import *

# Defineerin funkstiooni:
def viske_tulemus(külgede_arv):
    arv = randint(1,külgede_arv)
    return arv

# Küsin kasutajalt sisendi:
küsi_n = int(input("Sisesta, mitu tahku on täringul: "))
küsi_m = int(input("Sisesta, mitu korda soovid visata: "))

# Kontrollin, kas sisend vastab tingimustele:
while True:
    if küsi_n in range(6, 13, 2):
        külg = küsi_n
        break
    else:
        print("Valitud tahkude arv ei vasta tingimustele.")
        küsi_n = int(input("Sisesta, mitu tahku on täringul: "))
        
while True:
    if küsi_m in range(2, 6):
        viskeid = küsi_m
        break
    else:
        print("Valitud visete arv ei vasta tingimustele.")
        küsi_m = int(input("Sisesta, mitu korda soovid visata: "))

# Leian visete tulemused ja nende summa:
järjend = []
kokku = 0
i = 0
while i < viskeid:
    tulemus = viske_tulemus(külg)
    print(tulemus)
    järjend.append(tulemus)
    kokku += tulemus
    i += 1

# Kontrollin, kas kõik visked on sama tulemusega:
j = 1
while j < len(järjend):
    if järjend[j] == järjend[j-1]:
        veel_juurde = (viskeid + külg - 2) ** 2
        j += 1
    else:
        break
    
    if veel_juurde:
        kokku = kokku + veel_juurde
    else:
        kokku = kokku

print("Visete summa: " + str(kokku))
    
