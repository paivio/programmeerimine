# Kuupäevade esitamisel tekib enim probleeme, kui kuupäev kirjutatakse kujul „05.06.2005“ – sellisel puhul pole võimalik aru saada, kas on mõeldud 5. juunit või hoopis 6. maid. Eestis ja enamikes teistes riikides kirjutatakse kuupäev reeglina formaadis DD.MM.YYYY, kuid Ameerika Ühendriikides on levinum järjekord MM.DD.YYYY. (Huvi korral vt https://en.wikipedia.org/wiki/Date_format_by_country.) Segaduse vältimiseks tuleks kuu nimi välja kirjutada.
# Kirjutada kõigepealt funktsioon kuu_nimi, mis võtab argumendiks kuu järjekorranumbri ja tagastab vastava kuu nime (väikeste tähtedega).
# Vihje: Seda funktsiooni saab kirjutada, kasutades vastuse andmisel if-lauseid, aga optimaalne lahendus oleks kasutada järjendit (siis ühtegi if-lauset vaja ei ole).
# Seejärel looge funktsioon kuupäev_sõnena, mis võtab argumendiks ühe sõnena esitatud kuupäeva formaadis “DD.MM.YYYY” (nt '24.02.1918') ning tagastab selle sama kuupäeva kujul <päev>. <kuu_nimi> <aasta>. a (nt '24. veebruar 1918. a'), kusjuures kuupäev_sõnena peab ühe toimingu delegeerima funktsioonile kuu_nimi. Abiks võib ka olla funktsioon split.
# Seejärel kirjutage programm, mis küsib kasutajalt kuupäeva kujul “DD.MM.YYYY” ning väljastab ekraanile vastava kuupäeva sõnena kujul<päev>. <kuu_nimi> <aasta>. a.

def kuu_nimi(kuup):
    järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    nimi = järjend[kuup - 1]
    return nimi



def kuupäev_sõnena(kuup):
    päev = kuup[:3]
    kuu_number = int(kuup[3:5])
    aasta = kuup[-4:]
    return(päev + " " + kuu_nimi(kuu_number) + " " + aasta + ". a")

kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(kuupäev_sõnena(kuupäev))
