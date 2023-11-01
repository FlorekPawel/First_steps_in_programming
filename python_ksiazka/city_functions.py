def city_country(city, country, population = 0):
    if population:
        combined = city.title() + ', ' + country.title() + ' - populacja ' + str(population)
    else: 
        combined = city.title() + ', ' + country.title()
    return combined