# 다수의 dict를 가진 리스트 data와 키 목록이 담긴 key_list가 주어진다. 
# data를 순회하여 얻은 dict를 key_list를 순회하여 얻은 값에 따라 아래 조건을 만족하는 코드를 작성하시오. 
# 만약 순회중인 dict에 key_list로 얻은 key가 없다면, 
# 해당 key에 'unknown' 문자열을 할당한다. 
# get 메서드와 setdefault 메서드를 활용한다. 
# 모든 상황에 대해 '{key} 은/는 {value}입니다.' 를 출력한다.


data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']


# 아래에 코드를 작성하시오.
for product in data:
    for key in key_list:
        if product.get(key) == None:
            product.setdefault(key,'unknown')
        print(f'{key}는 {product[key]}입니다.')