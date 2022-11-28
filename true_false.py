# count = count + 1

# print(f'Az 5-nél nagyobb számok: {count}')
# print("eldöntés - True/False")
# wr = open(eldöntés.txt,'w')
# t = [2,5,6,9,10,12,4]
# wr.write('t = [2,5,6,9,10,12,4]')
# n=len(t)
# wr.write(n)
# ker = 5
# wr.write('A keresett szám:{ker}')
# i = 0
# while i < n and t[i] != ker:
#     i = i + 1
# if i < n:
#     print("Van ilyen ", ker)
#     wr.write("Van ilyen ")
# else:
#     print("Nincs ilyen ", ker)
#     wr.write("Van ilyen ")



# print("kiválasztás")
# t = [2,5,6,9,10,12,4]
# n = len(t)
# ker = 5
# i = 0
# while t[1] != ker:
#     i = i+1
# print("ezen a helyen található ", i+1)



# print("lineáris keresés")
# print('eldöntés (van-nincs), kiválasztás tétel (hely megadás)')
# t = [2,5,6,9,10,12,4]
# n = len(t)
# print(n)
# ker = 5
# i = 0 
# while i < n and t[i] != ker:
#     i = i+1
#     if (i<n):
#         print(f'van {ker} elem a listában')
#         print(f'Helye {i+1}')
#     else:
#         print(f'nincs {ker} elem a listában')


# szélsőérték
t = [2,5,6,9,10,12,4]
maxElem=t[0]
for elem in t:
    if elem > maxElem:
        maxElem=elem
    print(maxElem)


minELem=t[0]
for elem in t:
    if elem < minELem:
        minElem=elem
    print(minElem)

print(f'Egyszerű számtani átlag: {(minElem + maxElem)/2}')




