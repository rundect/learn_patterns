# Пример непитонического кода.
spam = 43
if 42 < spam and spam < 99:
    print(spam)

# Пример питонического кода.
spam = 98
if 42 < spam < 99:
    print(spam)


# Пример питонического кода.
spam = eggs = bacon = 'string'
print(spam, eggs, bacon)
print(spam == eggs == bacon == 'string')


# Пример непитонического кода.
spam = 'cat'
if spam == 'dog' or spam == 'cat' or spam == 'mouse':
    print(spam)

# Пример питонического кода.
spam = 'cat'
if spam in ('dog', 'cat', 'mouse'):
    print(spam)
