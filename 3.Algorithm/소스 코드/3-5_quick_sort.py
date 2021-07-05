def partition(arr, left, right):
    low = left
    high = right+1
    pivot = arr[left]
    while True:
        while True:
            low += 1
            if low > right or arr[low] >= pivot:
                break
        while True:
            high -= 1
            if high < left or arr[high] <= pivot:
                break
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[left], arr[high] = arr[high], arr[left]
    return high

def quick_sort(arr, left, right):
    if left < right:
        q = partition(arr, left, right)
        quick_sort(arr, left, q-1)
        quick_sort(arr, q+1, right)

arr = [5,4,3,2,1,10,9,8,7,6,11]
'''
for randomly assigned array
>>> import numpy as np
>>> arr = np.random.randn(100)
'''
print('Before:', arr)
quick_sort(arr, 0, len(arr)-1)
print('After:', arr)
