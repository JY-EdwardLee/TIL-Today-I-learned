

def pre_order(n):   # 전위 순회
    if n:   # 0이 아니면
        result.append(n)    # 노드 결과값에 추가
        pre_order(left[n])  # 왼쪽 순회
        pre_order(right[n]) # 오른쪽 순회

# 인풋 받기
N = int(input())
arr = list(map(int, input().split()))
left = [0] * (N+1)      # 왼쪽 자식 키값
right = [0] * (N+1)     # 오른쪽 자식 키값

# 노드 개수-1(간선 개수) 만큼 순회
for i in range(N-1):
    # 부모(p) - 자식(c) 간선
    p, c = arr[i*2], arr[i*2+1]

    if left[p] == 0: # 부모 왼쪽 자식 없으면
        left[p] = c # 자식 키값 넣기
    else:   # 왼쪽 자식 있으면
        right[p] = c    # 오른쪽 자식 키값 넣기

result = []
pre_order(1)
print(' '.join(map(str, result)))