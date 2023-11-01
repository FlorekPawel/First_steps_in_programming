import json

def get_num():
    file = 'ul_liczba.json'
    liczba = input('podaj ulubiona liczbę: ')

    with open(file, 'w') as f_obj:
        json.dump(liczba, f_obj)
def load_num():
    file = 'ul_liczba.json'
    try:
        with open(file) as f_obj:
            liczba = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return liczba
def show_num():
    liczba = load_num()
    if liczba:
        odp = input("czy twoja ulubiona liczba to: " + liczba + '? tak/nie ')

        if odp == 'tak':
            print('znam twoją ulubiona liczbę, to: ' + liczba)
        else:
            liczba = get_num()
    else:
        get_num()
    
show_num()

