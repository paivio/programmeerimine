# Kui aadressile https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/ lisada kuunimi, siis sellelt aadressilt võib leida lehe, kus on kirjas selle kuu nimepäevalised.
# Kirjutada programm, mis
# küsib kasutajalt kuunime (võib eeldada, et kasutaja sisestab kuunime õigesti ja "märts" asemel kirjutab "marts"),
# küsib kasutajalt päeva (võib eeldada, et sisestatud kuus leidub sellise järjekorranumbriga päev),
# loeb vastavalt aadressilt selle kuu nimepäevad (kasulik oleks nendest koostada järjend, abiks võib olla meetod splitlines()) ja
# väljastab ekraanile sisestatud kuupäevale vastavad nimepäevalised.

from urllib.request import urlopen

kuu = input("Sisestage kuu: ")
päev = int(input("Sisestage päev: "))
aadress = "https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/" + kuu

fail = urlopen(aadress)
baidid = fail.read()
tekst = baidid.decode()
read = tekst.splitlines()
fail.close()

nimed = read[päev -1]

print("Kuupäeval " + str(päev) + ". " + kuu + " on nimepäevad järgmistel inimestel:")
print(nimed)