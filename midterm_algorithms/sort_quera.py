n = int(input())

final_result = [[1]]

last = [1, 1]

if n != 1:
    final_result.append([1, 1])
    
    for i in range(n - 2):
        
        new = [1]
        
        for index in range(len(last) - 1):
            new.append(last[index] + last[index + 1])
        
        new.append(1)
        last = new
        final_result.append(new)
        

for arr in final_result:
    arr = [str(i) for i in arr]
    print(" ".join(arr))