import numpy as np


arr = np.random.randn(20) * 5

# print(arr)

remainders, whole_part = np.modf(arr)


# print(remainders)

# print("==================")

# print(whole_part)

# # print(np.sqrt(whole_part))

# temp = np.sqrt(arr)

# print(np.isnan(temp))


def binary_search(array, item):
    func_data = {
        "low": 0,
        "high": len(array) - 1
    }
    
    while func_data["high"] >= func_data["low"]:
        middle = ((func_data["high"] + func_data["low"]) // 2)
        guess = array[middle]
        if guess == item:
            return middle
        elif guess > item:
            func_data["high"] = middle - 1
        elif guess < item:
            func_data["low"] = middle + 1
    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7], 34))
