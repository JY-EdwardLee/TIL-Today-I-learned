def ordered_difference_sets(set1, set2):
    set_list = [set1 - set2, set2 - set1]
    set_list.sort(key = len)
    return list(set_list)

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})