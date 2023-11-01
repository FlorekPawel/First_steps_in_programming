file_path = 'zad.txt'

with open(file_path) as file_object:
    text = file_object.read()
    print(text)

print('\n')

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')

with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

with open(file_path) as file_object:
    for line in file_object:
        line = line.replace('Moge', 'Mozesz')
        print(line)
    
