class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = eletkor_
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f'Az állat neve {self.nev} , {self.faj} fajba tartozik, {self.eletkor} éves, {self.elohely}-n él, {self.meret}méretű'
    
class Madar(Allat):
    def __init__(self, nev_, eletkor_,):
        super().__init__(nev_, 'madár', eletkor_, 'erdő', 'kicsi')

    def csiripel(self):
        print(f'{self.nev} csiripel')

class Keteltu(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, 'kétéltű', eletkor_, 'tópart', 'kicsi')

    def brekeg(self):
        print(f'{self.nev} brekeg')

class Hullo(Allat):
    def __init__(self, nev_, eletkor_, elohely_,):
        super().__init__(nev_, 'Hullo', eletkor_, elohely_, 'kicsi')

    def napozik(self):
        print(f'{self.nev} napozik a kövön')