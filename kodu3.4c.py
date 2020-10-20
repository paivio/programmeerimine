# Legend räägib, et malemängu leiutajale olla tollane valitseja pakkunud tasu. (Sellest legendist räägib ka Tõnu Tõnso paarikümne aasta taguses leheloos.)
# Leiutaja oli “tagasihoidlik” ja palus tasuks
# esimese ruudu eest 1 nisutera,
# teise ruudu eest 2 korda rohkem ehk 2,
# kolmanda ruudu eest veel 2 korda rohkem ehk 4,
# neljanda ruudu eest siis 8,
# viienda ruudu eest 16 jne
# Malelaual on 64 ruutu.
# Koostada programm, mis
# küsib kasutajalt ühe täisarvu;
# arvutab while-tsükli abil, mitu nisutera sellise järjekorranumbriga ruudu eest leiutaja küsis;
# tulemus väljastatakse ekraanile pärast tsüklit. 

arv = int(input("Sisetage täisarv: "))

ruut = 1
teri = 1

while ruut < arv:
    teri *= 2
    ruut += 1

print("Nisuteri " + str(arv) + ". eest: " + str(teri))
    