kanapka = ['chleb', 'szynka', 'szynka', 'szynka', 'ser']

while 'szynka' in kanapka:
    kanapka.remove('szynka')

for skł in kanapka:
    print(skł)

kanapka.insert(0, 'szynka')
for skł in kanapka:
    print('- ' + skł)