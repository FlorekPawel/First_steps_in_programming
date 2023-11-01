
class User():

    def __init__(self, imię, nazwisko, nick):
        self.imię = imię
        self.nazwisko = nazwisko
        self.nick = nick
        self.l_logowań = 0
    
    def describe_user(self):
        print('Użytkownik ' + self.imię.title() + self.nazwisko.title() + ' ma nick: ' + self.nick)

    def powitanie(self):
        print('Siema ' + self.nick + '!!!')
    
    def wzrost_prób_logowań(self):
        self.l_logowań += 1
 
    def reset(self):
        self.l_logowań = 0

