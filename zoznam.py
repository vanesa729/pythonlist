"""suciastky = ["rezistor", "kondenzator", "dioda", "tranzistor", "rele"]
print(type(suciastky))
print(suciastky)
print(suciastky[0])
print(suciastky[1:4])
print(len(suciastky) -1)
suciastky.append("poistka")
print(suciastky)
suciastky.insert(1, "poistka")
print(suciastky)
suciastky.extend(["spinac", "poistka"])
print(suciastky)
suciastky.remove("poistka")
print(suciastky)
odobrane = suciastky.pop()
print(odobrane)
print(suciastky)
novylist = []
novylist.append(suciastky.pop())
print(novylist)"""

"""merania = [4, 5, 8, 22, 3, 11]
vysoke = []
for i in merania [:] :
    if i > 10 :
        vysoke.append(i)
        merania.remove(i)
print("Ostali:", merania)
print("Vysoke", vysoke)"""

sklad = ["rezistor", "kondenzátor", "dióda", "tranzistor", "relé"]
servis = []

print("Počet súčiastok:", len(sklad))

print("Prvá:", sklad[0])
print("Posledná:", sklad[-1])

sklad.append("poistka")
sklad.insert(0, "cievka")

sklad.remove("dióda")

sklad[0], sklad[-1] = sklad[-1], sklad[0]

servis.append(sklad.pop())

i = 1
for s in sklad:
    print(f"{i}. {s}")
    i += 1
print("Na servise:", servis)

nazov = input("Zadaj súčiastku: ")
if nazov in sklad:
    sklad.remove(nazov)
    print("Vydané.")
else:
    print("Na sklade nie je.")
