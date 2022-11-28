import random

szam1 = input("Adj meg egy számot: ")
szam2 = random.randint(11,49,2)
szam3 = 6

print(szam1)
print(szam2)
print(szam3)

if (szam1%2):
    print('A szám páratlan')
else:
    print('A szám páros')


szamok=[szam1, szam2, szam3]
print(szamok)


#4
#a
szamok.append(4)
szamok.append(5)
szamok.append(6)
for i in range(7, 9):
    szamok.append(i)

#b
szamok.extend((4, 5, 6))
for i in range(7, 9):
    szamok.append(i)
print(szamok)

#c
szamok.insert(3, 4)
szamok.insert(4, 5)
szamok.insert(5, 6)
print(szamok)

#d
szamok.pop(4)
szamok.insert(4, 'négyes')
szamok.insert(5, 'ötös')
szamok.insert(6, 'hatos')
print(szamok)

#e
print(min((1, 2, 3)))
print(max((1, 2, 3)))

print(szamok)


#5
halmaz={szam1,szam2,szam3}
#a
ebed = set(['halászlé', 'kenyér', True])
#b
halmaz.add('13')
#c
halmaz.remove('13')
#d
halmaz.discard('13')
#e
halmaz.pop()

print(halmaz)


wr = open("maskamate.txt", "w")
wr.write(szam1)
wr.write(szam2)
wr.write(szam3)



