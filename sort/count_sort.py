# Count Sort
    # 1- when can put items to seprate groups
    # 2- when (count of items) >> (count of groups)


# implements

import random

data = [random.randint(0, 200) for i in range(1000000)]

# maximum = max(data)

# you can use max function of find maximum your self

maximum = 0

for num in data:
    if num > maximum:
        maximum = num

count = [0] * (maximum + 1)

for number in data:
    count[number] += 1


print(count) # this list will contain count of all values
