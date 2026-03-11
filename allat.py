class Allatok:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = eletkor_
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f'Az állat neve {self.nev} , {self.faj} fajba tartozik,\n {self.eletkor} éves, {self.elohely}-en él, {self.meret}méretű'        