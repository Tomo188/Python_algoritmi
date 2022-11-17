def sorting(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


a = [[[0, 2, 1, 4, 4], [2, 5, 1, 76, 1, 3, 4, 1]]]


def twoDimensional(arr):
    for i in arr:


l            twoDimensional(i)
else:
    sorting(arr)


print(type(a) == list)
twoDimensional(a)
print(a)
