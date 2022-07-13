
cat_file = 'catssdfg.txt'
dog_file = 'dogs.txt'

try:
    with open(cat_file) as f:
        contest = f.read()
except FileNotFoundError:
    pass
else:
    print(contest)
