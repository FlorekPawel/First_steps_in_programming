class Employee():
    def __init__(self, imię, nawzwisko, pensja):
        self.imię = imię.title()
        self.nawzwisko = nawzwisko.title()
        self.pensja = pensja
    
    def give_raise(self, podwyżka = 5000):
        self.pensja += podwyżka
