def f(i, n, k):
    # global count
    if i == n:
        print(arr)
        # count += 1
        # if count == k:
        #     result = arr
        #     return result
    else:
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            answer = f(i + 1, n, k)
            if answer:
                return answer
            arr[i], arr[j] = arr[j], arr[i]

# count = 0
arr = [num for num in range(1, 4)]
print(f(0, 3, 5))