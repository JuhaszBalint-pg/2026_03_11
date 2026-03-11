from allat import Allat

class Emlos(Allat):
    def __init__(self, nev_, faj_, eletkor_, szorzetszine_, elohely_):
        #ősosztály, örökölt tulajdonságokat hordoz
        super().__init__(nev_, faj_, eletkor_, elohely_, 'közepes', )
        self.szorzetszine = szorzetszine_

    def __str__(self):
        return super().__str__() + f' a szőrzete: {self.szorzetszine}'
    

class Macska(Emlos):
    def __init__(self, nev_, eletkor_, szorzetszine_, elohely_):
        super().__init__(nev_, 'macska', eletkor_, szorzetszine_, elohely_)


    def dorombol(self):
        print(f'{self.nev} dorombol')
    
class Kutya(Emlos):
    def __init__(self, nev_, eletkor_, szorzetszine_, elohely_):
        super().__init__(nev_, 'kutya', eletkor_, szorzetszine_, elohely_)
    
    def ugat(self):
        print(f'{self.nev} ugat')