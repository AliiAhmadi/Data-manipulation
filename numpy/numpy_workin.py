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

# print(test_arr)

arr3d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# print(arr3d)

# arr3d[:, 1] = 12
# print(arr3d)


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

# print(names)


data = np.random.randn(7, 4)

# print(data)

# print(names == "Will")

# print(names == "Bob")
# print("-----------------------------")
# print(data[names == 'Bob'])
# print("-----------------------------")
# print(data)

# print(names != "Bob")
cond = names == 'Bob'
# print(cond)

# print(data[~cond])


second_test = (names == "Bob") | (names == "Will")

# print(second_test)


# print(data)

# print("----------------------------")
# data[data < 0] = 0

# print(data)

emp_arr = np.empty((8, 5))

# print(emp_arr)

for i in range(8):
    emp_arr[i] = i ** 3
    
# print(emp_arr)

# print(np.array([1, 2, 3, 4, 5, 6]))

# print(emp_arr)


array = np.arange(32).reshape((8, 4))

# print(array[[2], [3]])

printable = array[[1, 5, 7, 2]][:, [0, 3, 1, 2]]

# print(array)

# print("==========================================")
# # array[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
# print(printable)


# printable = np.arange(32).reshape(4, 8)


# print(printable)
# print("==================")
# print(printable.T)


printable = np.arange(32).reshape((2, 4, 4))

# print(printable.transpose((1, 2, 1)))

# print(printable)

# print("=========================")

# # print(printable.transpose((1, 0, 2)))


# print(printable.swapaxes(0, 1))


## ufuncs

array = np.arange(32)

# print(np.exp(array))

result = np.exp2(array)

# result = np.sqrt(array)

# print(array)

print(result)

# there is some unary ufuncs
 
 
# now lets see some binary ufuncs

