import random
import time

start = time.time()

secret = random.randint(1, 500)

print(f'Загадане число: {secret}')

for i in range(1, 1000000):
    print(i, end=" ")

end = time.time()

print(f'Час роботи програми: {round(end - start, 2)} сек.')

abs()
