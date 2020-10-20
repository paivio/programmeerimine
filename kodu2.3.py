# Inimese nimede osas on erinevatel maadel erinevaid kombeid ja vähemalt naabrite puhul oleks hea neid teada (areneva Balti koostöö mõttes).
# Traditsiooniliselt näitab leedu naiste perekonnanimedes nime lõpp perekonnaseisu. Näiteks on Adamkienė abielus ja Adamkutė mitte. Alates 2003. aastast on lubatud ka lühem vorm, mis perekonnaseisu ei näita, nt Adamkė. Huvi korral uuri lähemalt siit.
# Koostada programm, mis küsib kasutajalt Leedu perekonnanime ja väljastab ekraanile
# Abielus, kui nimi lõpeb tähtedega "ne",
# Vallaline, kui nimi lõpeb tähtedega "te",
# Määramata, kui nimi lõpeb tähega "e" (aga mitte "ne" ja "te"),
# Pole ilmselt leedulanna perekonnanimi, kui nimi ei lõpe tähega "e".

nimi = input("Sisestage Leedu perekonnanimi: ")

if nimi[-1] == "e":
    if nimi[-2:] == "ne":
        print("Abielus")
    elif nimi[-2:] == "te":
        print("Vallaline")
    else:
        print("Määramata")
else:
    print("Pole ilmselt leedulanna perekonnanimi")