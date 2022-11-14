'''
    Halmaz (set):
    - rendezetlen (elemeknek nincs indexe)
    - egy elem csak egyszer szerepelhet
    - többféle típust tárolhat egyszerre is
    - a halmaz eleme maga nem változtatható meg
    '''

# halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}

# üres halmaz létrehozása
# ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

# bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])
# egy elem hozzáadása
reggeli.add('lekvár')

# egy nem meghatározott elem eltávolítása
reggeli.pop()

# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')

# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')

reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

# metszet
print(reggeli & ebed)
# unio
print(reggeli | ebed)
# különbség
print(reggeli - ebed)
# csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)


# üres szótár létrehozása
raktar = {}
print(raktar)

# szótár létrehozása adatokkal
diak = {
    'vezeteknev': 'Kiss',
    'keresztnev': 'Péter',
    'eletkor': 17,
    'menza': True
}