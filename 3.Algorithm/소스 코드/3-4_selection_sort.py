def selection_sort(arr, current_index):
    min_index = current_index
    # Update min_index to indicate minimum value
    for i in range(min_index+1,len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    # Swap
    arr[current_index], arr[min_index] = arr[min_index], arr[current_index]
    if current_index+1 < len(arr):
        selection_sort(arr, current_index+1)

arr = [5,4,3,2,1]
'''
for randomly assigned array
>>> import numpy as np
>>> arr = np.random.randn(100)
'''
print('Before:', arr)
selection_sort(arr, 0)
print('After:', arr)