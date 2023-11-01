flag = True
file_name = 'guests'

while flag is True:

    imie = input('Podaj imię: ')
    print('Siema ' + imie + '!!!')
    if imie == 'koniec':
        flag = False
    
    with open(file_name, 'a') as file_object:
        file_object.write(imie + "\n")