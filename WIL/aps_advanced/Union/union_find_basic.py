class UnionFind():
    def __init__(self):
        pass

# 6개의 원소가 존재하는 경우

# 1. 집합을 만드는 함수
def make_set(n):
    # 1~n 까지의 원소가 있다고 가정 -> 총 n 개의 집합을 생성
    # --> 각 원소의 부모를 자신으로 초기화
    parents = [i for i in range(n + 1)]
    rank = [0] * (n + 1) # rank 전체 초기화

    return parents, rank


def find_set(x):
    # 기본 코드
    # # 기저조건: 자기 자신 == 부모노드 -> 해당 집합의 대표자
    # if parents[x] == x:
    #     return x    # 대표자를 return
    # return find_set(parents[x])     # 대표자를 return

    # 경로 압축 (Path compression) 코드
    # x의 부모를 대표자로 변경
    # parents[x] = find_set(parents[x])
    # 매번 모든 노드의 대표자를 변경
    while parents[x] != x:
        parents[x] =parents[parents[x]]
        x = parents[x]

    return x


def union(x, y):
    # 1. x와 y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면? 어차피 같은 결과
    if ref_x == ref_y:
        return
    # 다른 집합이라면 합친다.
    # -> 문제에 따라 우선되는 집합으로 합쳐주면 된다. (문제마다 다름)
    # --> 이번 예시: 더 작은 노드로 합친다.
    # if ref_x < ref_y:
    #     parents[ref_y] = ref_x
    # else:
    #     parents[ref_x] = ref_y
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        # 아무거나 설정하고 대표자의 rank += 1
        parents[ref_y] = ref_x
        ranks[ref_x] += 1

N = 6
parents, ranks = make_set(N)
# print(parents)  # 해당 노드의 부모 정보를 가진 리스트 출력

union(1, 3)
union(2, 3)
union(5, 6)

print(parents)

# 3과 5는 같은 집합인가요??
if find_set(3) == find_set(5):
    print("같은 집합입니다")
else:
    print("다릅니다")
