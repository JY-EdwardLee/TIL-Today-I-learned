T= int(input())


for tc in range(1, T+1):
    # 학생 수, 이동 횟수
    N = int(input())
    # [현재방, 원래방]을 담을 리스트
    rooms = []
    for _ in range(N):
        cnt, origin = map(int, input().split())
        # 현재방과 원래방 중 작은 쪽을 튜플의 앞쪽 원소로 저장
        if cnt < origin:
            rooms.append((cnt, origin))
        else:
            rooms.append((origin, cnt))
    # 학생이 이동을 완료했는지 점검
    visited = [0]*N
    # 단위시간
    count = 0
    while 0 in visited:     # 모든 학생이 이동했다면
        corridor = [0] * 201    # 복도의 방을 짝지어서 생성
        for i in range(N):      # 학생을 순회
            cnt, origin = rooms[i]      # cnt와 origins에 각각 방 번호 추가
            if visited[i] == 1:     # 처리된 학생이면
                continue    # 넘어가고
            if 1 in corridor[(cnt+1)//2:(origin+1)//2 + 1]:     # 다른 학생이 지나가서 부딪힐 예정이면
                continue    # 넘어가고
            visited[i] = 1      # 보낸 학생은 visited 표기
            for j in range((cnt+1)//2, (origin+1)//2 + 1):      #학생이 지나갈 복도를 1표기
                corridor[j] = 1
        else:   # 한 싸이클 다 보내면
            count += 1      # 단위 시간 +1
    print(f'#{tc} {count}')