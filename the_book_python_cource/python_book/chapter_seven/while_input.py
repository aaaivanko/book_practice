
places = {}

active = True

while active:

    name = str(input('Please write your name: '))
    best_place = str(input('Please write your best place: '))

    places[name] = best_place

    exit = input('if you want to exit press exit')

    if exit != 'exit':
        continue
    else:
        active = False


for name, place in places.items():
    print(name, place)
