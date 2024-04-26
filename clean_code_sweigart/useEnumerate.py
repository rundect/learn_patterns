# not pythonic
animals = ['cat', 'dog', 'mouse']
for i in range(len(animals)):
    print(i, animals[i])

# pythonic
animals = ['cat', 'dog', 'mouse']
for i, animal in enumerate(animals):
    print(i, animal)
