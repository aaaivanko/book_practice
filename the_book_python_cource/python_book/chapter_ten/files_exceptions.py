
file_name = 'guest.txt'

with open(file_name, 'a') as file_object:
    while True:
        name = str(input('Please write your name: (press q to exit)'))
        if name == 'q':
            break
        else:
            file_object.write(f"Hello, {name}!\n")
