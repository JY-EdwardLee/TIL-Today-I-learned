
def get_count(a, b, c):
    eating = 0
    if b == 1 or 1 <= c <= 2:
        return -1
    if a < b < c:
        return 0
    if b >= c:
        eating += b - c + 1
        b = c - 1
    if a >= b:
        eating += a - b + 1
    return eating

# 1 < 2 < 3
T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    print(f'#{tc} {get_count(A, B, C)}')