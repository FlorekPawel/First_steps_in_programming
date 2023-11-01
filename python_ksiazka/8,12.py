def make_car(marka, model, **inne):
    car = {}
    car['marka'] = marka
    car['model'] = model
    for key, value in inne.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)