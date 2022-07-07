
cities = {
    'kiev': {
        'location': 'Ukraine',
        'population': 3_000_000,
    },
    'berlin': {
        'location': 'Ukraine',
        'population': 3_000_000,
    }
}

for city, infos in cities.items():
    print(f'\n{city}')
    for key, value in infos.items():
        print(f'\t{key} {value}')