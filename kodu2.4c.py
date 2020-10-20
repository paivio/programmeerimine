# Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks.
# Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).

inimesi = int(input("Inimeste arv: "))
kohti = int(input("Kohtade arv: "))

if inimesi % kohti == 0:
    busse = inimesi // kohti
    print("Busse vaja: " + str(busse))
    print("Viimases bussis inimesi: " + str(kohti))
else:
    busse = (inimesi // kohti) + 1
    viimases = inimesi % kohti
    print("Busse vaja: " + str(busse))
    print("Viimases bussis inimesi: " + str(viimases))
