# Selection Sort


# Implements

import random

MIN = 0
MAX = 10000
LOOP = 1000

data = [random.randint(MIN, MAX) for i in range(LOOP)]

for i in range(len(data) - 1):
    selection = i
    for j in range(i + 1, len(data)):
        if data[j] < data[selection]:
            selection = j
    data[i], data[selection] = data[selection], data[i]


print(data)