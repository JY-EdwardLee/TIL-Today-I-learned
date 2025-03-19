

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    p = arr[0]

    smaller, bigger = [], []

    for x in arr:
        if x == p:
            continue
        if x < p:
            smaller.append(x)
        else:
            bigger.append(x)

    left = quickSort(smaller)
    right = quickSort(bigger)

    return left + [p] + right

arr = [6, 9, 5, 1, 3, 13, 10]
print(quickSort(arr))