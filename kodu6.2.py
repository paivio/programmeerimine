# Optimaalseks kauguseks teleri ja vaataja silmade vahel arvatakse olevat 2,5 korda ekraani diagonaali pikkus. Seega kui on teada kaugus diivanist teleri asukohani, siis teleri sobiva diagonaali saab arvutada järgmise valemi järgi:
# (teleri diagonaal tollides) = (kaugus meetrites) * 100 * 0,39 / 2,5
# Defineerige funktsioon nimega teleri_diagonaal, mis võtab argumendiks ühe arvu, mis tähistab kaugust diivanist teleri asukohani meetrites ning arvutab selle põhjal teleri diagonaali tollides ja tagastab selle.
# Tagastatud teleri diagonaal peab olema ümardatud täisarvuni. Ümardamist peab sooritama funktsioon ise ja selleks tuleb kasutada funktsiooni round.
# Rakendage loodud funktsiooni programmis, kus kaugus diivanist telerini (meetrites) küsitakse kasutaja käest. Väljastage teleri diagonaal (tollides) ekraanile.
# Oluline on, et teleri diagonaali arvutamise funktsioon ise ei küsiks kasutajalt midagi ja see funktsioon ise ka ei väljastaks tulemust ekraanile. Need tegevused peab tegema programmis väljaspool funktsiooni, funktsiooni töö on vaid arvutada.

def teleri_diagonaal(x):
    diagonaal = round(kaugus * 100 * 0.39 / 2.5)
    return diagonaal

kaugus = float(input("Sisesta kaugus: "))
print(teleri_diagonaal(kaugus))