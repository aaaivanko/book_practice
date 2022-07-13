import json

filename = 'username.json'


def get_stored_username():
    """Get stored username"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you when you come back {username}")


def greet_user():
    """Greet user or create file!"""
    username = get_stored_username()
    if not username:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We will remember you when you come back {username}")
    else:
        print(f"Welcome back {username}")
        new_user = input(f'If you are not {username} press new otherwise press whatever you want: ')
        if new_user == 'new':
            get_new_username()
        else:
            pass


greet_user()