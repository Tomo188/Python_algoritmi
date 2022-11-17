def insertionSort(arr, start, end, target):
    import math
    mid = math.floor((start + end) / 2)
    if mid == (len(arr)-1) and arr[mid] != target:
        return -1
    if mid == 0 and arr[mid] != target:
        return -1
    if arr[mid] > target:
        index = insertionSort(arr, start, mid-1, target)
    elif arr[mid] < target:

        index = insertionSort(arr, mid+1, end, target)
    else:
        print("found", mid)
        return mid
    return index


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(insertionSort(arr, 0, len(arr), 7))
