import random


COUNT = 100
MAXIMUM = 100000000
COUNT_PER_ONCE = 100

def sort_change_count(data):
    counter = 0
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and data[j] > temp:
            data[j + 1], j = data[j], j - 1
            counter += 1
        data[j + 1] = temp
    
    return counter



results = []

for num in range(COUNT):
    data = [random.randrange(MAXIMUM) for i in range(COUNT_PER_ONCE)]
    results.append(sort_change_count(data))

print(sum(results) / len(results))
    
