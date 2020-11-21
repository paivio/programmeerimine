# Kirjutage funktsioon ühisosa, mis võtab argumendiks kaks järjendit ning tagastab uue järjendi, mis sisaldab (ühekordselt) neid väärtusi,
# mis esinevad mõlemas järjendis.

def ühisosa(järjend1, järjend2):
    ühisosa_hulk = set()
    for i in range(len(järjend1)):
        if järjend1[i] in järjend2:
            ühisosa_hulk.add(järjend1[i])
    ühisosa_järjend = list(ühisosa_hulk)
    return ühisosa_järjend


a = [1, 2, 3, 4, 5, 6, 5, 4, 6]
b = [2, 4, 6, 8, 5]

print(ühisosa(a, b))
