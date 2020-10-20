# Mõned õpetajad on tavatsenud õpilasi tahvli juurde vastama kutsuda kuupäeva järgi vastavalt õpilaste nimekirjale. Näiteks 4. kuupäeval tuleb esimesena vastama nimekirjas 4. olev õpilane. Failis nimekiri.txt on õpilaste nimed, igaüks eraldi real. Üks selline, mis on genereeritud leheküljel http://random-name-generator.info/, on siin. Võite ise koostada ka teistsuguse nimekirja.
# Koostada programm, mis
# küsib failinime (eeldame, et kasutaja sisestatud nimega fail leidub ja seal on vähemalt 31 nime);
# loeb sisestatud nimega failist andmed;
# väljastab vastavalt tänasele kuupäevale õpilase nime, kes peab vastama tulema. 

from datetime import *

päev = datetime.now().day
failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

nimekiri = []

for rida in fail:
    nimekiri.append(rida.strip("\n"))

print("Vastama tuleb: " + nimekiri[päev-1])
