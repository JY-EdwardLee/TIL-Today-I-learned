# union_sets 함수
# 두 개의 셋을 인자로 받아 합집합을 반환해야 한다.

# union_multiple_sets 함수
# 최소 두 개 이상의 셋이 제공되었는지 검사하고, 그렇지 않은 경우 "최소 두 개의 셋이 필요합니다."  라는 메시지가 출력되어야 한다.
# 넘겨받은 모든 셋을 순회하여 합집합을 진행한 결과를 반환한다.

# 아래 함수를 수정하시오.
def union_sets(set_1, set_2):
    return set_1.union(set_2)

def union_multiple_sets(*sets):
    new_set = set()
    if len(sets) < 2:
        print(f'최소 두 개의 셋이 필요합니다.')
    else:
        for data in sets:
            new_set = new_set.union(data)
        return new_set


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다

