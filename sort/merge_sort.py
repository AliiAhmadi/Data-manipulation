# Merge Sort

# Implements

import random

def merge_sort(data_list):
    if len(data_list) < 2:
        return data_list
    
    if len(data_list) == 2:
        if data_list[0] <= data_list[1]:
            return data_list
        if data_list[1] < data_list[0]:
            return [data_list[1], data_list[0]]
        
    mid = len(data_list) // 2
    first_half = data_list[:mid]
    second_half = data_list[mid:]
    
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    
    i = j = 0
    result_list = []
    while i < len(first_half) and j < len(second_half):
        if first_half[i] <= second_half[j]:
            result_list.append(first_half[i])
            i += 1
        else:
            result_list.append(second_half[j])
            j += 1
            
    result_list += first_half[i:] + second_half[j:]

    return result_list


unsorted_data = [random.randint(0, 10000) for i in range(1000)]

print(merge_sort(unsorted_data))