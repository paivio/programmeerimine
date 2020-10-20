# Koostada programm, mis kuvab valge taustaga graafikaakna pealkirjaga “Lipp” ja joonistab sinna vabalt valitud (vähemalt 3 värviga või mingi keerulisema kujundiga) Eesti haldusüksuse lipu (https://et.wikipedia.org/wiki/Eesti_haldusüksuste_lippude_loend).
# Lipul peab olema kasutatud vähemalt kolme värvi või mingit keerulisemat kujundit. Eks igaüks valib ise. Narva-Jõesuu lipp on päris tore väljakutse või hoopis Tartu või Palamuse. Soovitatav oleks valida lipp, kus on midagi korduvat, tsüklilist, et saaks kasutada tsükleid.

from tkinter import *

raam = Tk()
raam.title("Karksi valla lipp")
tahvel = Canvas(raam, width= 1200, height = 700)

i = 0

while i < 7:
    if i < 3:
        tahvel.create_rectangle(0, i * 100, 1200, (i + 1) *100, fill="#f7d117", outline="#f7d117")
    elif i < 4:
        tahvel.create_rectangle(0, i * 100, 1200, (i + 1) *100, fill="white", outline="white")
    else:
        tahvel.create_rectangle(0, i * 100, 1200, (i + 1) *100, fill="#00736b", outline="#00736b")
    i += 1

tahvel.pack()
raam.mainloop()