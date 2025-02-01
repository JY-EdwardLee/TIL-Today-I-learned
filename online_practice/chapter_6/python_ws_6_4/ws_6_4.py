# 아래 함수를 수정하시오.
def get_keys_from_dict(dict_):
    return list(dict_.keys())

def get_all_keys_from_dict(dict_):
    new_list = []
    for key in dict_:
        new_list.append(key)
        if type(dict_[key]) == type(dict_):
            new_list.extend(get_all_keys_from_dict(dict_[key]))
    return new_list

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
