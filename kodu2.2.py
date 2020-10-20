# Teemapargis on allveelaeva atraktsioon, kuhu pääsevad ainult inimesed, kes on lühemad kui 120 cm. Lisaks peab atraktsioonile pääsemiseks omama piletit või kaelakaarti.
# Koostada programm, milles
# küsitakse tema pikkust sentimeetrites,
# küsitakse, kas kasutaja omab kaelakaarti (kasutaja sisestab jah või ei),
# küsitakse, kas kasutaja omab piletit (kasutaja sisestab jah või ei),
# väljastatakse ekraanile Pääseb allveelaevale, kui kasutaja pääseb atraktsioonile, vastasel juhul väljastatakse Ei pääse allveelaevale.

pikkus = int(input("Sisesta pikkus: "))
kaart = input("Kas kasutaja omab kaelakaarti? ")
pilet = input("Kas kasutaja omab piletit? ")

if pikkus < 120 and (kaart == "jah" or pilet == "jah"):
    print("Pääseb allveelaevale")
else:
    print("Ei pääse allveelaevale")