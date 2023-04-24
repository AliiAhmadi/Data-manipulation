# Selection Sort

# in any step we choose one item and move it to the currect location

import random

MIN = 0
MAX = 1000000
LOOP = 2000

data = [random.randint(MIN, MAX) for i in range(LOOP)]

for index in range(1, len(data)):
    cp_index = index
    while cp_index > 0 and data[cp_index] < data[cp_index - 1]:
        data[cp_index], data[cp_index - 1] = data[cp_index - 1], data[cp_index]
        cp_index -= 1

print(data)
