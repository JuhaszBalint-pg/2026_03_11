from allat import Allat, Hullo, Madar, Keteltu
from emlos import Emlos, Macska, Kutya

allat1 = Allat('Bodri', 'kutya', 5, 'kert', 'Nagy')
allat2 = Allat('Cirmi', 'cica', 3, 'ház', 'közepes')

print(allat1)
print(allat2)

emlos1 = Emlos('Morzsi', 'Kutya', 5, 'kert', 'barna')
emlos2 = Emlos('Bözsi', 'boci', 10, 'Tarka', 'farm' )
print(emlos1)
print(emlos2)

kutya1 = Kutya('Negro', 4, 'Fekete', 'virágos hordó')
print(kutya1)
kutya1.ugat

macska1 = Macska('Rozi', 6, 'barna cirmos', 'tanya')
print(macska1)
macska1.dorombol

hullo1 = Hullo('Berci', 100, 'Alpok')
hullo1.napozik()

keteltu1 = Keteltu('Zsolti a béka', 7)
keteltu1.brekeg()

madar1 = Madar('Turul', 10)
madar1.csiripel()