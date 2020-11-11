failinimi = input("Sisestage failinimi: ")
KM = int(input("Sisestage riigi käibemaks: "))
alates_tagasi = int(input("Sisestage summa, millest alates saab käibemaksu tagasi: "))

def hind_käibemaksuga(neto, protsent):
    bruto = neto * (1 + protsent/100)
    return bruto

fail = open(failinimi, encoding="UTF-8")

neto_järjend = []

for i in fail:
    neto_järjend.append(float(i.strip("\n")))
    
summa = 0
j = 0
tagasi_summa = 0

while j < len(neto_järjend):
    bruto = hind_käibemaksuga(neto_järjend[j], KM)
    j += 1
    summa += bruto
    if bruto > alates_tagasi:
        tagasi = bruto - bruto/(1 + KM/100)
        tagasi_summa += tagasi
    
ümard_summa = round(summa, 2)
ümard_tagasi = round(tagasi_summa, 2)
    
print("Kokku on kulutatud: " + str(ümard_summa))
print("Tagasi saab: " + str(ümard_tagasi))
