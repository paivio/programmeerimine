### NB! NB! See ei ole lõplik versioon. Tulevad parandused!

#Arvutikontrolltöö nr 1 (variant 1).
# Päivi Ojala
# Ül 1

# Küsin failinime:
failinimi = input("Sisestage failinimi: ")

# Loen failist andmed:
fail = open(failinimi, encoding="UTF-8")

aastad = []
sünnid = []

for rida in fail:
    ridade_kaupa = rida.split(" ")
    aastad.append(int(ridade_kaupa[0]))
    sünnid.append(int(ridade_kaupa[1]))
fail.close()

# Arvutan, mitu last sündis:
i = 0
sündis_kokku = 0
while i < len(sünnid):
    sündis_kokku += sünnid[i]
    i += 1

# Milisel aastal sündis kõige rohkem lapsi:
# r = 0
# while r < len(sünnid):
#     if sünnid[r] > sünnid[r-1]:
#         suuremad = []
#         suuremad.append(sünnid[r])
#         r += 1
#     else:
#         r += 1
        
# Kõige suurema sündide arvuga aasta:
suurim = max(sünnid)

j = 0
while j < len(sünnid):
    if sünnid[j] == suurim:
        suurim_aasta = aastad[j]
        j += 1
    else:
        j += 1
    
# Kõige väiksema sündide arvuga aasta:
vähim = min(sünnid)

s = 0
while s < len(sünnid):
    if sünnid[s] == vähim:
        vähim_aasta = aastad[s]
        s += 1
    else:
        s += 1

# Tulemus:
print("Kokku sündis " + str(sündis_kokku) + " last.")
print("Kõige rohkem lapsi (" + str(suurim) + ") sündis aastal " + str(suurim_aasta) + ".")
print("Kõige vähem lapsi (" + str(vähim) + ") sündis aastal " + str(vähim_aasta) + ".")




        


        

    
    
    
    
    
    
    
    
