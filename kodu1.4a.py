# Ülikoolides arvestatakse ühe ainepunkti ajakuluks 26 tundi. Näiteks kolme ainepunkti kursusel on ajakuluks 3 * 26 = 78 tundi. Kui see jaotada 10 nädala peale on ühe nädala eeldatav ajakulu 78 / 10 = 7,8.
# Koostada programm, mis
# küsib kasutajalt just sellises järjekorras ainepunktide arvu (täisarvu) ja nädalate arvu (täisarvu);
# arvutab ja väljastab ekraanile ühe nädala eeldatava ajakulu, mis on ümardatud täisarvuni. 

punktid = int(input("Sisestage ainepunktide arv: "))
nädalad = int(input("Sisestage nädalate arv: "))
tunnid = punktid * 26

vastus = round(tunnid / nädalad)

print(vastus)
