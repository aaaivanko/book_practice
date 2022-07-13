import json

filename = 'best_number.json'


def get_stored_number():
    """Get favourite number wrote by user"""
    try:
        with open(filename) as f:
            best_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return best_number


def store_best_number():
    """Store best number"""
    with open(filename, 'w') as f:
        best_number = input("Please write your best number: ")
        json.dump(best_number, f)
        print(f"We will remember {best_number} when you will come back!")


def show_number():
    """Show best number"""
    best_number = get_stored_number()

    if best_number:
        print(f"Your best number is: {best_number}")
    else:
        store_best_number()


show_number()