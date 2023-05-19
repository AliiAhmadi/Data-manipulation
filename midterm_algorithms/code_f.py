n = int(input())

def is_is(number):
    number = str(number)
    number = set(number)
    if len(number) == 1:
        return True
    return False

counts = []

for i in range(n):
    inp = int(input())
    counter = 0
    for j in range(1, inp + 1):
        if is_is(j):
            counter += 1
    
    counts.append(counter)
    


for x in counts:
    print(x)