T= int(input())


def get_time()


for tc in range(1, T+1):
    N = int(input())
    stack = []
    que = []
    for _ in range(N):
        cnt_room, org_room = map(int, input().split())
        que.append((cnt_room, org_room))
    if que and cnt_room <= que[0][0] <= org_room:
        continue
    else:
        stack.append((cnt_room, org_room))
        cnt_room, org_room = que.pop(0)
