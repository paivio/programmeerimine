# Koostada programm, mille
# 1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2016 (arvuna);
# 2. real luuakse muutuja nimega lind ning antakse sellele väärtuseks "rasvatihane" (sõnena);
# 3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta lind on " (sõnena);
# 4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja lind (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
# 5. real väljastatakse muutuja lause väärtus ekraanile.

aasta = 2016
lind = "rasvatihane"
lause_keskosa = ". aasta lind on "
lause = str(aasta) + lause_keskosa + lind
print(lause)
