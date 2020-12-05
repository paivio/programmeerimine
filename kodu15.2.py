# Kirjutada funktsioon sümbolite_sagedus, mis võtab argumendiks sõne ja tagastab sõnastiku, mis sisaldab selles sõnes esinevate tähtede esinemiste
# sagedusi. Sõnastiku võtmeteks on tähed või muud sümbolid (ehk sõned pikkusega 1) ja väärtusteks täisarvud, mis näitavad, mitu korda vastavad
# sümbolid sõnes esinesid.

def sümbolite_sagedus(sõne):
    sagedus = {}
    sümbolid = []
    for i in sõne:
        loendur = 1
        võti = i
        sümbolid.append(i)
        if i in sagedus:
            loendur += 1
            if i in sümbolid:
                loendur = sagedus[võti] + 1
        sagedus[võti] = loendur
    return sagedus