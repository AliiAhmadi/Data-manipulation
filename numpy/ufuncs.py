import numpy as np


arr = np.random.randn(20) * 5

# print(arr)

remainders, whole_part = np.modf(arr)


# print(remainders)

# print("==================")

# print(whole_part)

# # print(np.sqrt(whole_part))

temp = np.sqrt(arr)

print(np.isnan(temp))
