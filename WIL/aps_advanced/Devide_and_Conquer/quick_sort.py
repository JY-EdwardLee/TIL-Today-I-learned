

def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l , r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)

def partition(arr, l, r):
    p = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]

    return j

arr = [6, 9, 5, 1, 3, 13, 10]
quickSort(arr, 0, len(arr)-1)
print(arr)quickSort()