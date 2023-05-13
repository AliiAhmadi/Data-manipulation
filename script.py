n = int(input())

names = []
amounts = []

for i in range(n):
    name, amount = input().split()
    amount = int(amount)
    names.append(name)
    amounts.append(amount)

maximum = max(amounts)

print(names[amounts.index(maximum)])