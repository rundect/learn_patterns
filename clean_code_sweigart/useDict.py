# Пример непитонического кода
numberOfPets = {'dogs': 2}
if 'cats' in numberOfPets:  # Проверить, существует ли ключ 'cats'.
    print('I have', numberOfPets['cats'], 'cats.')
else:
    print('I have 0 cats.')


# Пример питонического кода.
numberOfPets = {'dogs': 2}
print('I have', numberOfPets.get('cats', 0), 'cats.')


# Пример непитонического кода
numberOfPets = {'dogs': 2}
if 'cats' not in numberOfPets:
    numberOfPets['cats'] = 0
numberOfPets['cats'] += 10
print(numberOfPets['cats'])


# Пример питонического кода
numberOfPets = {'dogs': 2}
numberOfPets.setdefault('cats', 0)
numberOfPets['cats'] += 10
print(numberOfPets['cats'])

