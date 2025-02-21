T= int(input())


for tc in range(1, T+1):
    N = int(input())
    cnt_room_list = []
    org_room_list = []
    dist_room = []
    stack = []
    for _ in range(N):
        cnt_room, org_room = map(int, input().split())
        cnt_room_list.append(cnt_room)
        org_room_list.append(org_room)
    count = 0
    visited = [0] * N
    while 0 in visited:
        check = 0
        time = [0] * 401
        M = len(dist_room)
        while True:
            if visited[check] == 1:
                check += 1
                if 0 not in visited:
                    count += 1
                    break
                continue
            if cnt_room_list[check] < org_room_list[check]:
                if (1 not in time[cnt_room_list[check]:org_room_list[check]+1]):
                    for i in range(cnt_room_list[check], org_room_list[check]+1):
                        if i%2 == 1:
                            time[i], time[i+1] = 1, 1
                        else:
                            time[i-1], time[i] = 1, 1
                    visited[check] = 1
            else:
                if (1 not in time[org_room_list[check]:cnt_room_list[check]+1]):
                    for i in range(org_room_list[check], cnt_room_list[check]+1):
                        if i%2 == 1:
                            time[i], time[i+1] = 1, 1
                        else:
                            time[i-1], time[i] = 1, 1
                    visited[check] = 1
            check += 1
            if (0 not in time) or (check == N):
                count += 1
                break
    print(f'#{tc} {count}')