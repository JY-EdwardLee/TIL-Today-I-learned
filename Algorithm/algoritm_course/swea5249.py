import sys
sys.stdin = open("input.txt", "r")
import heapq

def optimus_prim(s):
    nodes = [s]
    cost = 0
    gan_lines = adj_List[s]
    while len(nodes) != V+1:
        w, e = heapq.heappop(gan_lines)
        if s in nodes and e in nodes:
            continue
        cost += w
        if s in nodes:
            for ganline in adj_List[e]:
                heapq.heappush(gan_lines, ganline)
            nodes.append(e)
            s = e
        else:
            for ganline in adj_List[s]:
                heapq.heappush(gan_lines, ganline)
    return cost


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_List = [[] for _ in range(E + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        heapq.heappush(adj_List[n1], (w, n2))
        heapq.heappush(adj_List[n2], (w, n1))
    print(f'#{tc} {optimus_prim(0)}')