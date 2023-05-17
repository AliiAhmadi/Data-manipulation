import math

def is_prime(number):
    if number == 1:
        return False
    flag = 0
    for k in range(2, int(math.sqrt(number)) + 1):
        if number % k == 0:
            flag = 1
            break
    
    if flag == 0:
        return True
    return False


n = int(input())

number = 10 ** (n - 1)

result = []

while len(str(number)) == n:
    flag = 0
    string = str(number)
    for i in range(n):
        if not is_prime(int(string[: n - i])):
            flag = 1
            break
        
    
    if flag == 0:
        result.append(string)
    number += 1

for i in result:
    print(i)