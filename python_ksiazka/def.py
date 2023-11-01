def poka_magika(magicy):
    for magik in magicy:
        print(magik.title())

def ulepszenie(słabi,ulepszeni):
    for slaby in słabi:
        lepszy = 'doskonały ' + slaby
        ulepszeni.append(lepszy)
    return ulepszeni

imiona = ['pawel', 'adolf', 'jozef']
ulepszeni = []
ulepszenie(imiona, ulepszeni)
poka_magika(ulepszeni)

x = 'paweł'
print(x.strip('aa'))