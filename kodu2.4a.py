# Tervisesport on tervisele kasulik, kui sellega jäädakse mõõdukuse piiridesse. On erinevaid variante sobiva koormuse valimiseks. Näiteks saab kasutada sellist arvestust, et maksimaalne pulsisagedus on meestel 220 miinus vanus ja naistel 206 miinus 88% vanusest. Seejuures erinevate treeningutüüpide puhul peaks pulsisagedus jääma järgmistesse vahemikesse:
# tervisetreening 50-70% maksimaalsest pulsisagedusest,
# põhivastupidavuse treening 70-80% maksimaalsest pulsisagedusest,
# intensiivne aeroobne treening 80-87% maksimaalsest pulsisagedusest.
# Koostada programm, mis küsib kasutajalt
# vanuse (täisarvuna aastates),
# soo (kasutaja sisestab M, m, N või n),
# treeningu tüübi (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening)
# ja lõpuks väljastab pulsisageduse vahemiku vastavatel tingimustel formaadis <vähim pulss> kuni <suurim pulss>, kus vastuses leiduvad arvud on ümardatud täisarvudeks.

vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ")
tüüp = int(input("Sisestage treeningu tüüp: "))

if sugu == "M" or sugu == "m":
    max_pulss = 220 - vanus
else:
    max_pulss = 206 - 0.88 * vanus
    
if tüüp == 1:
    pulss_alumine = round(0.5 * max_pulss)
    pulss_ülemine = round(0.7 * max_pulss)
elif tüüp == 2:
    pulss_alumine = round(0.7 * max_pulss)
    pulss_ülemine = round(0.8 * max_pulss)
else:
    pulss_alumine = round(0.8 * max_pulss)
    pulss_ülemine = round(0.87 * max_pulss)
    
print("Pulsisagedus peaks olema vahemikus " + str(pulss_alumine) + " kuni " + str(pulss_ülemine) + ".")