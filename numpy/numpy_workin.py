import numpy as np


test_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(test_arr.dtype)

# test_arr = test_arr.astype(np.str_)

# print(test_arr)

# test_range = np.arange(10, dtype=np.float64)

# print(test_range)


# empty = np.empty((3, 5), dtype=np.uint32)

# print(empty.dtype)

test_arr2 = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

# print(test_arr)
# print(test_arr2)
# print(test_arr < test_arr2)

test_arr[0][2:12] = 10000
# test_arr[0][:] = 10000

print(test_arr)