arr = [69, 10, 30, 2, 16, 8, 31, 22]

# 1. 분할 : 리스트 길이가 1이 될 때까지 분할
def merge_sort(arr):
    # 기저 조건 : arr이 한개만 남았을 때는 하나 남은 arr 값을 return
    if len(arr) == 1:
        return arr
    left, right = [], []        # 1. 분할하게 될  left, right 리스트 생성
    middle = len(arr)//2        # 2. 전체 arr에서 중앙으로 나누기
    for x in arr[:middle]:      # 3-1. 0 ~ 중간 -1 까지 left
        left.append(x)
    for x in arr[middle:]:      # 3-2. 중간 ~ 끝까지 right
        right.append(x)

    # mid = len(arr)//2
    # left, right = arr[:mid], arr[mid:]
    #
    # left = merge_sort(left)     # left 영역에서 1~3 반복
    # right = merge_sort(right)   # right 영역에서 1~3 반복

    # print(left, right)  # ((([a], [b]),([c], [d])),([e], [f]),([g], [h]))))
    return merge(left, right)


#2. 병합 : 병합하면서 작은 원소부터 추가
def merge(left, right):
    # result = [] # 병합할 리스트 생성
    #
    while len(left) > 0 or len(right) > 0:      # left or right가 빌 때까지 진행
        # 둘다 값이 있을 땐 result에 작은 값 추가
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 한 쪽만 값이 있으면, 한쪽 값 추가
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    # result = [0]*(len(left) + len(right))
    # l = r = 0
    #
    # while l < len(left) and r < len(right):
    #     if left[l] < right[r]:
    #         result[l+r] = left[l]
    #         l += 1
    #     else:
    #         result[r+l] = right [r]
    #         r += 1
    # while l < len(left):
    #     result[l+r] = left[l]
    #     l += 1
    # while r < len(right):
    #     result[l+r] = right[r]
    #     r += 1

    return result


print(merge_sort(arr))
