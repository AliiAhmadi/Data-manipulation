# insertion sort

# without any limitation


# implements

import random

MIN = 0
MAX = 1000000
LOOP = 2000

data = [random.randint(MIN, MAX) for i in range(LOOP)]

for i, value in enumerate(data):
    if i == 0:
        continue
    k = i
    while k > 0 and data[k - 1] > value:
        data[k] = data[k - 1]
        k -= 1
    data[k] = value


print(data) # print sorted numbers

