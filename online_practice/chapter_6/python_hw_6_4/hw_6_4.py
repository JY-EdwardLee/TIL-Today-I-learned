# 아래 함수를 수정하시오.
def add_item_to_dict(dict_, key_, value_):
    dict_[key_] = value_
    new_dict = dict_.copy()
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
