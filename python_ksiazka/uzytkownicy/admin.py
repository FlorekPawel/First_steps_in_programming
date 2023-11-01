from users import User

class Moce():
    def __init__(self, moce):
        self.moce = moce

    def show_moce(self):
        for moc in self.moce:
            print('- ' + moc)


class Admin(User):

    def __init__(self, imię, nazwisko, nick):
        super().__init__(imię, nazwisko, nick)
        self.moce = Moce(['banować', 'zmieniać regulamin', 'dodawać nowych ludzi'])
    
