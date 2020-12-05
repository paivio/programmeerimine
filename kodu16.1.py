# Sõiduki registreerimismärgile või riigi tunnusmärgile on tavaliselt märgitud riigi tähis 1-3-tähelise lühendina. Eesti puhul on lühendiks
# näiteks EST. Piirivalvel on andmebaas eri riikide tähistest tekstifailis nii, et faili igal real on tühikuga eraldatud riigi tähis ja selle
# riigi nimi.
# Väljavõte riigitähiste failist:
# ER Eritrea
# FIN Soome
# F Prantsusmaa
# H Ungari
# LT Leedu
# EST Eesti
# S Rootsi
# Kirjutada funktsioon failist_sõnastik, mis võtab argumendiks failinime ning tagastab vastava faili sisu põhjal sõnastiku, kus võtmeteks on
# riigitähised ja väärtusteks riikide nimed.
# Kirjutada funktsioon tähised_nimedeks, mis võtab argumendiks järjendi riikide tähistest ja eelmise funktsiooni poolt koostatud sõnastiku ning
# tagastab järjendi vastavate riikide nimedest. Kui mõni tähis on tundmatu, siis selle riigi nimi asendada tagastatavas järjendis väärtusega None.
# Rakendada funktsioone sobivalt programmis, mis küsib kasutajalt esiteks andmebaasi failinime ja teiseks sõne, mis koosneb tühikutega eraldatud
# piiri ületanud sõidukite riikide tähistest, ning väljastab sõidukite päritolumaade nimed üksteise alla. Kui mõni riigitähis on tundmatu, siis
# väljastada selle riigi nime asemel Tundmatu maa.

def failist_sõnastik(failinimi):
    fail = open(failinimi, encoding="UTF-8")
    sõnastik = {}
    for i in fail:
        rida = i.split()
        võti = rida[0]
        väärtus = rida[1]
        sõnastik[võti] = väärtus
    fail.close()
    return sõnastik

def tähised_nimedeks(järjend, sõnastik):
    uus_järjend = []
    for i in järjend:
        if i in sõnastik:
            nimi = sõnastik[i]
            uus_järjend.append(nimi)
        else:
            uus_järjend.append(None)
    return uus_järjend
            
riigid = input("Riigitähiste faili nimi: ")
tähised = input("Piiri ületanud sõidukite tähistused: ")
sõnastik = failist_sõnastik(riigid)
järjend = tähised.split()

vastus = tähised_nimedeks(järjend, sõnastik)
for i in vastus:
    if i == None:
        print("Tundmatu maa")
    else:
        print(i)
