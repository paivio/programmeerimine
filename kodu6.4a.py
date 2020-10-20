# Muuta ülesandes 6.1 koostatud programmi nii, et tervitamisel lisatakse ka, mitmes tervitus käsil on. Selleks tuleb funktsioonile tervitus lisada argument, seda funktsioonis sobivalt kasutada ja igal tsükli sammul tuleb funktsioon välja kutsuda ühe võrra suurema argumendiga kui eelmisel korral.

def tervitus(j):
    print('Võõrustaja: "Tere!"')
    print("Täna " + str(j) + ". kord tervitada, mõtiskleb võõrustaja")
    print('Külaline: "Tere, suur tänu kutse eest!"')
    
arv = int(input("Sisesta külastajate arv: "))

i = 0
j = 1

while i < arv:
    tervitus(j)
    i += 1
    j += 1