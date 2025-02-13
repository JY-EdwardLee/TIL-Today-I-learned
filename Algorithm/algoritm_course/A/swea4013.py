import sys
sys.stdin = open("../input.txt", "r")

T = int(input())


def clockwise(arr):
    # 시계방향으로 돌릴 시 [7, 0, 1, 2, 3, 4, 5, 6]
    arr.insert(0,arr.pop(-1))
    return arr

def c_clockwise(arr):
    # 반시계방향으로 돌릴 시 [1, 2, 3, 4, 5, 6, 7, 0]
    x = arr.pop(0)
    arr.append(x)
    return arr


for tc in range(1, T+1):
    K = int(input())
    # 자석 정보
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    # 점검하는 인덱스 : red_arrow (고정)
    red_arrow = 0

    # 회전 할 때마다 상태 업데이트 하기
    for _ in range(K):
        mag, direction = map(int, input().split())
        left = mag - 1
        right = mag - 1
        # 돌지 말지 점검
        whether = [0] * 4
        whether[mag - 1] = direction
        # 왼쪽 점검 2 <-> 6
        while 0 < left:
            if magnetics[left][6] != magnetics[left-1][2]:
                whether[left-1] = whether[left]*(-1)
                left -= 1
            else:
                break
        # 오른쪽 점검
        while right < 3:
            if magnetics[right][2] != magnetics[right+1][6]:
                whether[right+1] = whether[right]*(-1)
                right += 1
            else:
                break
        # 돌리기
        for gear in range(4):
            if whether[gear] == 1:
                magnetics[gear] = clockwise(magnetics[gear])
            elif whether[gear] == -1:
                magnetics[gear] = c_clockwise(magnetics[gear])
    score = [1, 2, 4, 8]
    total_score = 0
    for i in range(4):
        total_score += magnetics[i][red_arrow]*score[i]
    print(f'#{tc} {total_score}')