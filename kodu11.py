# Koostada funktsioon leidub_anagramm, mis võtab argumendiks sõnede maatriksi (listide listi), milles sõned koosnevad vaid tähtedest a, b, c ja d, ning tagastab tõeväärtuse vastavalt sellele, kas selles maatriksis leidub element, mis on sellise sõne anagramm, mis on saadud temast vahetult vasakul ja vahetult paremal olevate sõnede kokkukirjutamise teel.
# Kui vasakul või paremal elementi ei leidu, siis arvestada seda tühja sõnena.

def leidub_anagramm(maatriks):
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            if j == 0:
                vasakul = ""
            else:
                vasakul = maatriks[i][j-1]
            if j == len(maatriks[i])-1:
                paremal = ""
            else:
                paremal = maatriks[i][j+1]
            if sorted(maatriks[i][j]) == sorted(vasakul + paremal):
                return True
    return False
 
 
a = [["ab", "cad", "cd"], ["abd", "a", "bd"]]
b = [["ab", "cad", "cd"], ["a", "bad", "bd"]]
c = [["ab", "ba"]]


print(leidub_anagramm(a))
print(leidub_anagramm(b))
print(leidub_anagramm(c))