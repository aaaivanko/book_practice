
def cars(name, year, **car_info):
    car_info['name'] = name
    car_info['year'] = year

    return car_info


print(cars('suzuki', 1994, color='blue', dorrs=6))
