first = int(input())
second = int(input())

def print_s(first, second):
    pass

if second > first:
    print("Wrong order!")
elif (first - second) % 2 != 0:
    print("Wrong difference!")
else:
    print_s(first, second)
