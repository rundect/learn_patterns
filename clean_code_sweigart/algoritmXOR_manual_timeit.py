import time

startTime = time.time()  # Сохранение времени запуска.
for i in range(1000000):  # Код выполняется 1 000 000 раз.
    a, b = 42, 101
    a = a ^ b
    b = a ^ b
    a = a ^ b
print(time.time() - startTime, 'seconds')  # Вычисление затраченного времени.
