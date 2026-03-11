from allat import Allat, Hullo, Madar, Keteltu
from emlos import Emlos, Kutya, Macska

allatok = []
with open('állatok/adatok/allatok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, faj, eletkor, szorzetszine = sor.strip().split(',')
        if faj == 'kutya':
            allatok.append(Kutya(nev, int(eletkor), szorzetszine, elohely_='kert'))
        elif faj == 'macska':
            allatok.append(Macska(nev, int(eletkor), szorzetszine, elohely_='padlás'))
        elif faj == 'madar':
            allatok.append(Madar(nev, int(eletkor),))
        elif faj == 'keteltu':
            allatok.append(Keteltu(nev, int(eletkor)))
        elif faj == 'hullo':
            allatok.append(Keteltu(nev, int(eletkor)))

for allat in allatok:
    print(allat)
    if isinstance(allat, Kutya):
        allat.ugat()
    elif isinstance(allat, Macska):
        allat.dorombol()
    if isinstance(allat, Madar):
        allat.csiripel()
    if isinstance(allat, Hullo):
        allat.napozik()
    if isinstance(allat, Keteltu):
        allat.brekeg()