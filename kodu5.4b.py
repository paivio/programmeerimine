# Noor mitmevõistleja on sel aastal kümnevõistluse läbinud kaks korda ja alade kaupa saadud punktid on järjendites: käärikul = [401, 604, 547, 700, 722, 845, 621, 490, 800, 700] ja kohilas = [900, 0, 333, 803, 838, 400, 467, 488, 432, 700].
# Koostada programm, mis
# koostab nende järjendite põhjal paremate tulemuste järjendi, milles igale kohale võetakse vastav parem tulemus (näitejärjendite puhul algab paremate tulemuste järjend [900, 604 ... );
# väljastab ekraanile paremate tulemuste järjendi ja paremate tulemuste järjendi elementide summa.

käärikul = [401, 604, 547, 700, 722, 845, 621, 490, 800, 700]
kohilas = [900, 0, 333, 803, 838, 400, 467, 488, 432, 700]

tulemus = []

for i in range(10):
    if käärikul[i] > kohilas[i]:
        tulemus.append(int(käärikul[i]))
    else:
        tulemus.append(int(kohilas[i]))

print(tulemus)
print(sum(tulemus))        
    