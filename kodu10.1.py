# Koostada funktsioon vahimatest_suurim, mis võtab argumendiks täisarvude maatriksi (listide listi) ja tagastab antud maatriksist kõikide ridade vähimatest elementidest suurima.
# Teisisõnu peab tagastatav element olema
# vähim element oma reas,
# suurim element kõikide selliste elementide seas, mis on oma reas vähimad.

def vahimatest_suurim(maatriks):
    väiksed = []
    suured = []
    for i in maatriks:
        väike = min(i)
        väiksed.append(väike)
        suur = max(väiksed)
    return suur
    
test = [[1,2,3],[4,5,6],[7,8,9],[10,11]]
print(vahimatest_suurim(test))