import sys
sys.stdin = open("../input.txt", "r")

def get_max(nums, trade):
    t, start = 0, 0       # 카드 변경 횟수, 카드 변경 시작 범위
    N = len(nums)
    while trade > t:
        # 기저조건? 카드 전체 점검 완료 시 맨 뒷자리 두개만 바꿔주기
        if start >= N:  # 시작 변경 범위가 전부 확인 완료하여 카드 길이보다 길어질 시
            nums[-1], nums[-2] = nums[-2], nums[-1]
            t += 1  # 변경 횟수 + 1
            continue
        # 범위 내 최댓값의 인덱스와 최소값의 인덱스 위치 바꾸기
        max_idx = []    # 점검 범위의 최댓값이 속한 인덱스의 모음
        for i in range(start, N):
            if nums[i] == max(nums[start:]):
                max_idx.append(i)
        chance = len(max_idx)   # 최댓값이 여러개 일 수도 있음
        if chance == 1 and max_idx == [start]:  # 최댓값이 점검 범위의 맨 앞에 혼자 있어서 변경이 의미가 없을 때
            start += 1  # 넘어가고 다음 범위 점검
            continue
        for _ in range(chance): # 바꿀 수 있는 기회는 최대값의 개수와 같음
            t += 1  # 변경 횟수 + 1
            c = nums.index(min(nums[start:start + chance])) # 점검 범위 중 가장 작은 값과
            d = max_idx.pop()                               # 최댓값 중 가장 뒤에 있는 값을
            nums[c], nums[d] = nums[d], nums[c]             # 바꿔주기
            if t == trade:  # 변경 횟수 한도 도달 시 정지
                break
        start += chance # 변경한 위치만큼 시작지점 옮기기


T = int(input())
for tc in range(1, T+1):
    n, trade = map(str, input().split())
    nums = list(map(int, n))
    trade = int(trade)
    get_max(nums, trade)
    print(f'#{tc} {"".join(map(str, nums))}')
