
current_users = ['Jester', 'Romned', 'Belosnezka', 'Devilie', 'Polkadot']

lover_curent_users = [item.lower() for item in current_users]


new_users = ['Bob', 'Romned', 'Dillan', 'Devilie', 'Sem']

if new_users:
    for new_user in new_users:
        if new_user.lower() in lover_curent_users:
            print(f'Sorry name {new_user} is already taken, please choose another one!')
        else:
            print(f'You can choose {new_user} its free!')

