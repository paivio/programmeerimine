# Failis sunnikuupaevad.txt on mingi hulk sünnikuupäevi, iga sünnikuupäev eraldi real. Kirjutada programm, mis tekitab selle faili põhjal 9 tekstifaili nimedega eluteenumber1.txt, eluteenumber2.txt, ..., eluteenumber9.txt ning jagab sünnikuupäevad nendesse failidesse vastavalt elutee numbrile (elutee numbri arvutamiseks kasutada funktsiooni elutee). Näiteks sünnikuupäev 15.05.1975 tuleb kirjutada faili eluteenumber6.txt.

def elutee(s):
    n = 0
    for i in s:
        if i != ".":
            n += int(i) 
    if n < 10:
        return n
    else:
        return elutee(str(n))
    
kuupäevad_failist = open("sunnikuupaevad.txt", encoding="UTF-8")
elutee1 = open("eluteenumber1.txt", "a", encoding="UTF-8")
elutee2 = open("eluteenumber2.txt", "a", encoding="UTF-8")
elutee3 = open("eluteenumber3.txt", "a", encoding="UTF-8")
elutee4 = open("eluteenumber4.txt", "a", encoding="UTF-8")
elutee5 = open("eluteenumber5.txt", "a", encoding="UTF-8")
elutee6 = open("eluteenumber6.txt", "a", encoding="UTF-8")
elutee7 = open("eluteenumber7.txt", "a", encoding="UTF-8")
elutee8 = open("eluteenumber8.txt", "a", encoding="UTF-8")
elutee9 = open("eluteenumber9.txt", "a", encoding="UTF-8")

for rida in kuupäevad_failist:
    number = elutee(rida.strip("\n"))
    if number == 1:
        elutee1.write(rida)
    elif number == 2:
        elutee2.write(rida)
    elif number == 3:
        elutee3.write(rida)
    elif number == 4:
        elutee4.write(rida)
    elif number == 5:
        elutee5.write(rida)
    elif number == 6:
        elutee6.write(rida)
    elif number == 7:
        elutee7.write(rida)
    elif number == 8:
        elutee8.write(rida)
    else:
        elutee9.write(rida)
    
kuupäevad_failist.close()
elutee1.close()
elutee2.close()
elutee3.close()
elutee4.close()
elutee5.close()
elutee6.close()
elutee7.close()
elutee8.close()
elutee9.close()