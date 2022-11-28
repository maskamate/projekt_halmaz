ev= [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650,]

#ev=False
if len(ev) == 12:
    #ev = True
    print(f'ez egy év adatsora')
else:
    print(f'ez nem egy év adatsora')


legnagyobb = ev[0]
for szam in ev:
        if szam > legnagyobb:
            legnagyobb = szam
print(f'legnagyobb:{legnagyobb}')

legkisebb = ev[0]
for szam in ev:
        if szam < legnagyobb:
            legnagyobb = szam
print(f'legkisebb:{legkisebb}')

osszeg = 0
for szam in ev:
    osszeg+= szam
print(osszeg)

count = 0
for szam in ev:
    if szam < 2400:
        count +=1
print(f'Ennyi van összesen: {count}')


hossz = len(ev)
ker = legnagyobb
i = 0
while ev[1] != ker:
    i+=1
print(f'legnagyobb helye: {+1}')

hossz = len(ev)
ker = legkisebb
i = 0
while ev[1] != ker:
    i+=1
print(f'legkisebb helye: {+1}')

wr = open("ev.txt", "w")
wr.write(f'ez egy év adatsora')
wr.write(f'ez nem egy év adatsora')
wr.write(f'legnagyobb:{legnagyobb}')
wr.write(f'legkisebb:{legkisebb}')
wr.write(osszeg)
wr.write('Ennyi van összesen: {count}')
wr.write()
wr.write()
wr.write()
wr.write()
wr.write()
wr.write()
wr.write()