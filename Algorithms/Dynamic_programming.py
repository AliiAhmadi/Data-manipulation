def fib(count: int):
    fibunatchi = [0, 1, 1]
    if count <= 2 and count >= 0:
        return fibunatchi[count]
    
    for index in range(3, count + 1):
        fibunatchi.append(fibunatchi[index - 1] + fibunatchi[index - 2])
    
    return fibunatchi[count]



print(fib(123))