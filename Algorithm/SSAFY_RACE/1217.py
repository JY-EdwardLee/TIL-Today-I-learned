

for tc in range(1, 11):
    test_case = input()
    N, M = map(int, input().split())
    print(f'#{test_case} {N ** M}')