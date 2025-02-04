T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a = map(int, input().split())
    data = list(a)
    sum_data = 0
    for number in data:
        sum_data = sum_data + number
    mean_data = sum_data/len(data)
    print(f'#{test_case} {int(round(mean_data, 0))}')
    # ///////////////////////////////////////////////////////////////////////////////////