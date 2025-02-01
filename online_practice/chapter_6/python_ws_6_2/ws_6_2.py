# 딕셔너리와 키를 인자로 받아 해당 키에 대응하는 값을 반환해야 한다.
# 조회하고자 하는 키가 딕셔너리에 존재하지 않는 경우, 'Unknown' 값을 반환해야 한다.

# 아래 함수를 수정하시오.
def get_value_from_dict(dict_, key):
    my_dict = dict_.copy()
    return my_dict.get(key,'unknown')


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown
