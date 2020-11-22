# Kirjuta funktsioon max_pikkus, mis võtab argumendiks listi, mille elementideks võivad olla täisarvud või listid, mille elementideks võivad
# olla täisarvud või listid, mille jne. Funktsioon peab tagastama pikima selles puntras leiduva listi pikkuse.

def max_pikkus(järjend):
    kõige_pikem = len(järjend)
    for i in range(len(järjend)):
        if isinstance(järjend[i], list):
            pikkus = max_pikkus(järjend[i])
        else:
            pikkus = len(järjend)
        if pikkus > kõige_pikem:
            kõige_pikem = pikkus
    return kõige_pikem


a = [[], [3,[4,5],[2,3,4,5,3,3], [7], 5, [1,2,3], [3,4]], [1,2,3,4,5]] # õige vastus 7 - OK
b = [[[1,2,3]]] # õige vastus 3 - OK
c = [1,2,3] # õige vastus 3 - OK
d = [[], [3, [4, 5], [2, 3, 4, 5, 3, 3, [], 3], [7], 5, [1, 2, 3], [3, 4]], [1, 2, 3, 4, 5]] # õige vastus 8 - OK
e = [[]] # õige vastus 1 - OK
 
print(max_pikkus(a))
print(max_pikkus(b))
print(max_pikkus(c))
print(max_pikkus(d))
print(max_pikkus(e))