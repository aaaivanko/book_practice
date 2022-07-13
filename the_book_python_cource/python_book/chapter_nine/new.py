from random import choice


def lottery(your_ticket):

    lottery_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd')
    number_iteration = 0
    winning_ticket = []

    while True:
        number_iteration += 1
        for item in range(4):
            winning_ticket.append(choice(lottery_tuple))
        print(winning_ticket)
        if your_ticket == winning_ticket:
            print(f"You win and it took you {number_iteration} times!")
            break
        else:
            winning_ticket = []

# lottery_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd')
#
# winning_ticket = []
#
# for item in range(4):
#     winning_ticket.append(choice(lottery_tuple))
#
# print(winning_ticket)


lottery([1, 5, 'a', 6])


