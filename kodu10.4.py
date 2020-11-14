# Kirjutada rekursiivne funktsioon paarissumma, mis võtab argumendiks ühe arvu a ja tagastab kõikide positiivsete paarisarvude summa, mis on väiksemad või võrdsed a-ga.
# Oma funktsiooni saate lihtsalt testida, kirjutades sama funktsionaalsusega mitterekursiivse funktsiooni ning kontrollides, kas need funktsioonid annavad sama tulemuse näiteks väärtuste a=1…1000 korral.

def paarissumma(a):
    summa = 0
    i = 0
    while i <= a:
        if a % 2 == 0:
            return paarissumma(a - 2) + a
        else:
            b = a - 1 
            return paarissumma(b - 2) + b
        i += 2
    return summa


print(paarissumma(9))


# Testimiseks ilma rekursioonita:
def paarissumma_test(a):
    summa = 0
    i = 0
    while i <= a:
        if a % 2 == 0 and i == 0:
            summa += a
        elif a % 2 == 0:
            a -= 2
            summa += a
        else:
            a -= 1
            summa += a
        i += 1
    return summa


print(paarissumma_test(9))