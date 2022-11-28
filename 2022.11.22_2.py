aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]
print(aug)
# Lehet e augusztus havi hóméséklet

if len(aug) == 31:
    #ev = True
    print(f'ez lehet augusztus havi hőmérséklet')
else:
    print(f'ez nem lehet augusztus havi hőmérséklet')


# A legnagyobb hóméséklet

legnagyobb = aug[0]
for szam in aug:
        if szam > legnagyobb:
            legnagyobb = szam
print(f'legnagyobb:{legnagyobb}')


# A legkisebb hóméséklet
legkisebb = aug[0]
for szam in aug:
        if szam < legkisebb:
            legkisebb = szam
print(f'legkisebb:{legkisebb}')


# Hány alkalommal volt a hőmeséklet 31 fok felett?
count = 0
for szam in aug:
    if szam > 31:
        count +=1
print(f'Ennyi van összesen: {count}')


# mekkora volt a hómérséklet augusztus 20.-án?
hossz = len(aug)
ker = legkisebb
print(f'augusztus 20-án', hossz, 'fok volt')


# mekkora volt az átlag hőmérséklet?
osszeg = 0
for szam in aug:
    osszeg+= szam
print(osszeg)

atlag = osszeg/31
print(f'átlag hőmérséklet: ', atlag)


# mekkora volt a hőingadoszás?
ing = legnagyobb - legkisebb
print(f'A hőingadozás: ', ing)

wr = open("aug.txt", "w")
wr.write(f'ez lehet augusztus havi hőmérséklet')
wr.write(f'ez nem lehet augusztus havi hőmérséklet')
wr.write(f'legnagyobb:{legnagyobb}')
wr.write(f'legkisebb:{legkisebb}')
wr.write(f'Ennyi van összesen: {count}')
wr.write(f'augusztus 20-án', hossz, 'fok volt')
wr.write(f'átlag hőmérséklet: ', atlag)
wr.write(f'A hőingadozás: ', ing)
wr.write()

wr.close
