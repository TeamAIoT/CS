def linear_search(arr, target):
    found = False
    for i in range(len(arr)):
        if arr[i] == target:
            found = True
            return i
    if not found:
        return -1


arr = [1,2,3,4,5]
target = 5
idx = linear_search(arr,target)

if idx != -1:
    print('Found! Value:{}, Index:{}'.format(target,idx))
else:
    print('Not Found!')