def greedy():
    cnt = 0                                 # 신청 개수 카운트용 변수
    while time:                             # 전부 조회하고 나면 종료
        e, s = time.pop(0)                  # 가장 종료시간이 빠른 팀부터 pop
        if times[s] != 0 or times[e] != 0:  # times 상에서 사용가능(0)이 아니면 다음 팀
            continue
        for i in range(s, e):               # 가능하면 바꿔놓고 cnt += 1
            times[i] = 1
        cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    o, e = map(int, input().split())    # 체육관 개방시간 o, e
    N = int(input())                    # 참가팀 N (=사용신청 개수)
    time = []                           # 사용신청 list
    for _ in range(N):                  # 사용신청 list 받기, 종료시간 먼저 넣기
        si, fi = map(int, input().split())
        time.append((fi, si))
    time.sort()                         # 종료시간 순으로 정렬
    times = [-1]*24                     # 24시간 count 만들기
    for i in range(o, e+1):             # 사용 가능한 시간만 0으로 세팅
        times[i] = 0
    print(f'#{tc} {greedy()}')