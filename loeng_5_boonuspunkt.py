# Ülesanne: Kui palju on veerusummade keskmisest väiksemaid veerusummasid?

# Algtabel:
tabel_ridadena = [[2, 3, 8, 5], [7, 5, 1, 9], [1, 6, 9, 2], [1, 5, 7, 0]]

# Teen algtabeli veerud ridadeks (sest ridadega on lihtsam arvutada):
for i in tabel_ridadena:
    tabel_veergudena = [[tabel_ridadena[j][i] for j in range(len(tabel_ridadena))] for i in range(len(tabel_ridadena[0]))]

# Leian veergude summad:
veeru_summad = []
for i in range(len(tabel_veergudena)):
    veerg = []
    for j in range(len(tabel_veergudena[i])):
        veerg.append(int(tabel_veergudena[i][j]))
    summa = sum(veerg)
    veeru_summad.append(summa)
    
# Leian keskmise veerusumma:
keskmine = sum(veeru_summad) / len(veeru_summad)

# Kui palju on keskmisest väiksemaid:
mitu = 0
for i in range(len(veeru_summad)):
    if veeru_summad[i] < keskmine:
        mitu += 1
        
# Vastus:
print("Veerusummade keskmisest väiksemaid veerusummasid on " + str(mitu) + ".")
