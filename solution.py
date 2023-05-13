n = int(input())

result = []

for i in range(1, n + 1, 2):
    starts = i
    spaceInEachSide = (n - i) // 2
    string = (spaceInEachSide * " ") + (starts * "*") + (spaceInEachSide * 2 * " ") + (starts * "*")
    result.append(string)


for string in result:
    print(string)

result.reverse()
result.pop(0)

for string in result:
    print(string)