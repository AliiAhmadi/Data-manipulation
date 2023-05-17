n, m = (int(i) for i in input().split())

hs = [int(i) for i in input().split()]

string = input()

##################

# functions

def right_to_left():
    for index in reversed(list(range(n))):
        if hs[index] < max(hs[index:]):
            hs[index] += 1
        


def left_to_right():
    for index in range(n):
        result = hs[:index]
        result.append(0)
        if hs[index] < max(result):
            hs[index] += 1






####################

for char in string:
    if char == "R":
        right_to_left()
    else:
        left_to_right()


hs = [str(num) for num in hs]

print(" ".join(hs))