# Kirjuta funktsioon listid_sõnastikuks, mis võtab argumendiks kaks ühepikkust listi ning tagastab nende põhjal moodustatud sõnastiku, kus
# võtmeteks on esimese listi elemendid ja väärtusteks teise listi vastavatel positsioonidel olevad elemendid. Kui võtmete listis on korduvaid
# elemente, siis sõnastikku panna neist viimane koos vastava elemendiga väärtuste listist.

def listid_sõnastikuks(list1, list2):
    sõnastik = {}
    for i in range(len(list1)):
        võti = list1[i]
        väärtus = list2[i]
        sõnastik[võti] = väärtus
    return sõnastik
