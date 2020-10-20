# Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks on vaja 5 täringut, Crapsi jaoks aga 2 täringut.
# Koostada programm, mis
# küsib kasutajalt vajalike täringute arvu;
# viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis jäävad 1 ja 6 vahele);
# väljastab iga arvu eraldi reale.

from random import randint

täringuid = int(input("Täringute arv: "))

i = 0

while i < täringuid:
    tulemus = randint(1, 6)
    print(tulemus)
    i += 1