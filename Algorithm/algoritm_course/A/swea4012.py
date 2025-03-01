# 값 구하는 함수
def get_score(comb):
    M = len(comb)
    result = 0
    # 들어온 원소 중 2개 조합 나오면
    for l in range(1<<M):
        subset_2 = []
        for k in range(M):
            if l & (1<<k):
                subset_2.append(comb[k])
        else:
            # 나올 때마다 점수 더해주기
            if len(subset_2) == 2:
                result += (arr[subset_2[0]][subset_2[1]] + arr[subset_2[1]][subset_2[0]])
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 부분 집합 중 조건에 알맞는 애들 담을 리스트
    comb_list = []
    # 부분 집합 중 원소의 개수가 N/2 녀석들 구하기
    for i in range(1<<N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(j)
        else:
            if len(subset) == N//2:
                comb_list.append(subset)
    count = len(comb_list)  # 부분집합 길이
    min_diff = float('inf')     # 최소 차이 기본값 세팅
    # 부분집합의 앞에 출발, 뒤에서 출발하면 짝 맞춰짐
    for comb1, comb2 in zip(comb_list[:count//2], comb_list[count-1:count//2-1:-1]):
        # 최소값 찾기
        min_diff = min(abs(get_score(comb1) - get_score(comb2)), min_diff)
    print(f'#{tc} {min_diff}')