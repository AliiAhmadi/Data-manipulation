# Bubble sort

# Implements

import random

MIN = 0
MAX = 10000
LOOP = 1000

data = [random.randint(MIN, MAX) for i in range(LOOP)]

for j in range(len(data)):
    is_changed = False
    for i in range(len(data) - 1, j, -1):
        if data[i] < data[i - 1]:
            data[i], data[i - 1] = data[i - 1], data[i]
            is_changed = True
    if not is_changed:
        break

print(data)