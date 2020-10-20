# Vabaõhuetendusel saavad vaatajad istuda põhja- või lõunatribüünil. Pileti ostmisel küsitakse kõigepealt, kas inimene tahab ise valida kummal tribüünil ta istub või see loositakse. Kui inimene tahab ise valida, siis järgmisena küsitakse, kas põhja- või lõunatribüünil. Kui ta ei taha valida, siis loositakse tribüün nii, et 2/3 tõenäosusega on see põhjatribüün ja 1/3 tõenäosusega lõunatribüün.
# Koostada programm, mis järgib ülaltoodud tingimusi ja väljastab ekraanile, millisele tribüünile istuda ja kas valik oli tahtlik või loosiga.
# Kui kasutaja valis tribüüni ise, siis tuleb väljastada Valisite ise, vastasel juhul Pilet loositi.
# Kui kasutaja soovib ise tribüüni valida, siis kirjutab ta esimesele küsimusele vastuseks ise, kui soovib loosida, siis kirjutab midagi muud.
# Kui kasutaja soovib valida põhjatribüüni, siis kirjutab ta vastuseks p ja kui soovib lõunatribüüni, siis kirjutab ta midagi muud.

from random import randint

valik = input('Kui soovite ise valida kummal tribüünil istuda, siis sisestage "ise": ')

if valik == "ise":
    tribüün = input('Kui soovite põhjatribüünile, siis sisestage "p": ')
    if tribüün == "p":
        print("Valisite ise. Pilet on põhjatribüünile")
    else:
        print("Valisite ise. Pilet on lõunatribüünile")
else:
    loos = randint(1,3)
    if loos == 1:
        print("Pilet loositi. Pilet on lõunatribüünile")
    else:
        print("Pilet loositi. Pilet on põhjatribüünile")