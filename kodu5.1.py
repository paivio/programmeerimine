# 2015. aastal registreeriti Eestis 685 uut mopeedi (http://www.stat.ee/34654). Kuude kaupa on arvud listis
# registreeritud = [4, 22, 84, 130, 128, 108, 80, 59, 37, 19, 7, 7] .
# Koostada programm, mis
# küsib kasutajalt täisarvu, mis tähistab ühe kuu järjekorranumbrit (jaanuar 1, veebruar 2 jne);
# väljastab, mitu uut mopeedi sel kuul registreeriti.

registreeritud = [4, 22, 84, 130, 128, 108, 80, 59, 37, 19, 7, 7]

kuu = int(input("Palun sisestage mitmes kuu: "))
arv = registreeritud[kuu-1]

print(str(kuu) + ". kuul registreeriti " + str(arv) + " uut mopeedi.")