import timeit

use_xor = timeit.timeit(
    'a, b = 42, 101; '
    'a = a ^ b; '
    'b = a ^ b; '
    'a = a ^ b'
)
print(use_xor)

new_variable = timeit.timeit(
    'a, b = 42, 101; '
    'temp = a; '
    'a = b; '
    'b = temp'
)
print(new_variable)

best_choice = timeit.timeit(
    'a, b = 42, 101; '
    'a, b = b, a'
)
print(best_choice)
