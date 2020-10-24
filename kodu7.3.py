# Koostada EasyGUI graafilise kasutajaliidesega kalkulaatori programm, mis
# laseb kasutajal
# sisestada kaks täisarvu lõigus 1-10 (integerbox);
# nuppude abil valida liitmise, lahutamise või korrutamise vahel (buttonbox);
# väljastab arvutuse tulemuse (msgbox).

from easygui import *

esimene_arv = integerbox("Sisestage esimene täisarv lõigus 1-10: ", lowerbound = 1, upperbound = 10)
teine_arv = integerbox("Sisestage teine täisarv lõigus 1-10: ", lowerbound = 1, upperbound = 10)

nupud = ["+", "-", "*"]

tehe = buttonbox("Valige tehe: ", choices = nupud)

if tehe == "+":
    vastus = esimene_arv + teine_arv
elif tehe == "-":
    vastus = esimene_arv - teine_arv
else:
    vastus = esimene_arv * teine_arv
    
msgbox("Tehte tulemus on " + str(vastus) + ".")
  

