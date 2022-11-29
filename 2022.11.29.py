'''
ABC falva erdőmérnőke programmal szeretné meghatározni az októberi fakitermelés 
tervét favágó csapata számára. Írjon programot, amellyel az erdőmérnök a
következő problémákat tudja megoldani!
Hozza létre a megfelelő adatszerkezetetm amellyel a feladat megoldható. 
'''
import random
fa=[]

# 1 A kitermelés 50 és 100 m3 között lehetséges naponta októberben!
for i in range (31):
    fa.append(random.randint(50,100))
print(f'lista: ', {fa})
# 2 A legnagyobb fakitermelés mennyiségét a tervszerint
max=0
for num in fa:
    if num > max:
        max = num
print(f'A legnagyobb: ', {max})

# 3 A legkisebb fakitermelés mennyiségét a tervszerint 
min=0
for num in fa:
    if num < min:
        min = num
print(f'A legkisebb: ', min)
# 4 Hány alkalommal volt a fakitermelés mennyiségé 82 m3 felett?
count = 0
for szam in fa:
    if szam > 82:
        count +=1
print(f'Ennyi van összesen 82 m3 felett: {count}')

# 5 mekkora volt a fakitermelés mennyisége októberi 20.-án?
mennyiség = len(fa)
ker = 20
print(f'október 20-án', mennyiség, 'menyiségű fa volt')

# 6 mekkora volt a fakitermelés átlag mennyisége?
osszeg = 0
for szam in fa:
    osszeg+= szam
print(osszeg)

atlag = osszeg/31
print(f'átlag mennyiség: ', atlag)
# Fájl írása fa.txt néven az amelyben az összes eredmény szerepel!
wr = open("fa.txt", "w")
wr.write(f'lista: , {fa}\n')
wr.write(f'A legnagyobb: , {max}\n')
wr.write(f'A legkisebb: , {min}\n')
wr.write(f'Ennyi van összesen 82 m3 felett: {count}\n')
wr.write(f'október 20-án, {mennyiség}, menyiségű fa volt \n')
wr.write(f'átlag mennyiség: , {atlag}\n')