# Kirjutada programm, mis
# küsib kasutajalt failinime,
# loeb vastavast failist sõnumi ja
# väljastab selle ekraanile telegrammi stiilis. Teha tuleb asendused
# Ä, ä → AE
# Õ, õ, Ö, ö → OE
# Ü, ü → UE
# Kõik tähed tuleb muuta suurtähtedeks.
# Teisi märke ei muudeta.

failinimi = input("Sisestage faili nimi: ")
fail = open(failinimi, encoding="UTF-8")
 
for rida in fail:
    for täht in rida: 
        if täht == "Ä" or täht =="ä":
            print("AE", end = "")
        elif täht == "Ö" or täht == "ö" or täht == "Õ" or täht == "õ":
            print("OE", end = "")
        elif täht == "Ü" or täht == "ü":
            print("UE", end = "")
        else:
            print(täht.upper(), end = "") 
 
fail.close()