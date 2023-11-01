while True:
    x = input('podaj 1. liczbę: ')
    y = input('podaj 2. liczbę: ')

    try:
        z = int(x) + int(y)
    except:
        TypeError = print('podaj liczby nie litery')
    else:
        print(z)

        dalej = input('kontynuować? tak/nie ')

        if dalej == 'nie':
            break
