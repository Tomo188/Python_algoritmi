def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


a = [1, 4, 2, 6, 3, 2, 7, 8]
bubbleSort(a)
print(a)
