import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def sudoku(arr):
    # 행 검사
    for i in arr:
        if len(set(i)) != 9:
            return 0
    # 열 검사
    for j in range(9):
        col_set = set()
        for i in range(9):
            col_set.add(arr[i][j])
        if len(col_set) !=9:
            return 0
    # 3x3 검사
    bin = range(0, 7, 3)
    for x in bin:
        for y in bin:
            mini_board = set()
            for i in range(3):
                for j in range(3):
                    ny = y + j
                    nx = x + i
                    mini_board.add(arr[ny][nx])
            if len(mini_board) != 9:
                return 0
    return 1
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sudoku(arr)}')