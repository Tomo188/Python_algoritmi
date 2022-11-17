def merge(left, right):
    c = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if right[0] > left[0]:
                c.append(left[0])
                left.remove(left[0])
            elif right[0] <= left[0]:
                c.append(right[0])
                right.remove(right[0])
        else:
            for i in left:
                c.append(i)
                left.remove(i)

            for i in right:
                c.append(i)
                right.remove(i)
    return c


def mergeSort(arr):
    import math
    if len(arr) == 1:
        return arr
    middle = math.floor(len(arr)/2)
    left = mergeSort(arr[0:middle])
    right = mergeSort(arr[middle:])
    print(left, right)
    temp = merge(left, right)
    print(temp)
    return temp


print(mergeSort([2, 10, 5, 20, -100, 250, 20, 2, 3, 4, 5, 6, 7]))
