# Väiksematel üritustel on külaliste ühekaupa tervitamine lihtne. Suurematel üritustel võib ühekaupa tervitamine olla juba kurnavam tegevus. Ülesanne on esmalt koostada ilma argumentideta funktsioon tervitus(), mis kuvab väljakutsel ekraanile täpselt sellisel kujul tervituse ja vastuse.
# Võõrustaja: "Tere!"
# Külaline: "Tere, suur tänu kutse eest!"
# Seejärel koostada programm, mis
# küsib kasutajalt külaliste arvu;
# rakendab tsükli abil vastav arv kordi funktsiooni tervitus().

def tervitus():
    print('Võõrustaja: "Tere!"')
    print('Külaline: "Tere, suur tänu kutse eest!"')
    
arv = int(input("Sisesta külastajate arv: "))

i = 0

while i < arv:
    tervitus()
    i += 1
    