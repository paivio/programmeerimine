# Koostada programm, mis
# loeb failist nimega konto.txt andmed;
# väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis.

fail = open("konto.txt", encoding="UTF-8")

for rida in fail:
    if float(rida) > 0:
        print(rida)
        
fail.close()