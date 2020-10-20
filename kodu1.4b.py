# Liiklusseaduse järgi määratakse suurima lubatud sõidukiiruse ületamise korral hoiatustrahv, mille suurus eurodes saadakse lubatud sõidukiirust ületanud kilomeetrite arvu korrutamisel arvuga 3. Hoiatustrahvi maksimaalmäär on 190 eurot.
# Trahvimääradest on juttu siin.
# Koostada programm, mis
# küsib kasutajalt just sellises järjekorras nime (sõne), lubatud kiiruse (täisarvu) ja tegeliku kiiruse (täisarvu);
# arvutab trahvi vastavalt kasutajalt saadud andmetele ja ülaltoodud reeglitele;
# väljastab nime ja trahvi ekraanile. 

nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik iirus (km/h): "))

kiiruse_ületus = tegelik_kiirus - lubatud_kiirus
trahv_arvutus = kiiruse_ületus * 3

trahv_tegelik = min(190, trahv_arvutus)

print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv_tegelik) + " eurot.")
