

class Restauracja():

    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.liczba_ob = 0
        self.ilość_jedzenia = 0
    def opis(self):
        print('Restauracja ' + self.nazwa + ' serwuje: ' + self.rodzaj)
    
    def otwarcie(self):
        print('Restauracja ' + self.nazwa + ' pracuje w godzinach 9:00 - 20:00')

    def ust_l_gości(self, liczba):
        self.liczba_ob = liczba

    def dodanie_l_gości(self, liczba):
        self.liczba_ob += liczba

    def ust_il_jedzenia(self, ilość):
        self.ilość_jedzenia = ilość
    
    def dostawa(self, ilość):
        self.ilość_jedzenia += ilość
    
    def możliwość(self):
        self.max_gości = self.ilość_jedzenia / 2
        print(self.max_gości)
    
    def obsługa(self, goście):
        self.liczba_ob += goście
        self.ilość_jedzenia -= goście * 2


class Budka_z_lodami(Restauracja):
    def __init__(self, nazwa, rodzaj, smak):
        super().__init__(nazwa, rodzaj)
        self.smak = smak

    def smaki(self):
        print('Ta restauracja ma lody o smaku: ')
        for smak in self.smak:
            print('- ' + smak)
