# inp = input()

# keys = []

# counter = 0

# for i in range(9):
#     keys.append(input())


# for key in keys:
#     pass

def _sum(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return array[0] + _sum(array[1:])



# print(_sum([1, 2, 3, 4, 5, 12, 45, 67, 4444]))


def quick_sort(array):
    if len(array) < 2:
        return array
    
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([1,4,5,6,1,2,3,3,4]))