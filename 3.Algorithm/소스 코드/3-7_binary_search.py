def binary_search(arr, target, start, end):
    if start > end or target < arr[start] or target > arr[end]:
        return -1
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)

arr = [5,4,3,2,1]
sortedArr = sorted(arr)
target = 5
idx = binary_search(sortedArr, target, 0, len(arr) - 1)

if idx != -1:
    print('Found! Value:{}, Index:{}'.format(target,idx))
else:
    print('Not Found!')