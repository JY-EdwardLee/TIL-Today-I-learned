import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = API_KEY


    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    # params = {
    #     'auth' : api_key,
    #     'topFinGrpNo' : '020000',
    #     'pageNo': 1
    # }
    response = requests.get(url).json()
    return response
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)

data = get_deposit_products()

# key 값 조회하기
# response['result'].keys()

# 상품 리스트 부여하기
prd_list = data['result']['baseList']
pprint.pprint(prd_list)

# 옵션 리스트 부여하기
def make_option_list(response):
    option_dict = {
        "fin_prdt_cd" : "금융상품코드",
        "intr_rate_type": "저축 금리 유형",
        "intr_rate_type_nm": "저축 금리 유형명",
        "save_trm": "저축 기간",
        "intr_rate": "저축 금리",
        "intr_rate2": "최고 우대금리"
    }

    optionList = [] # 상품/옵션이 들어갈 빈 리스트

    # 한글 변환하기
    for prd in response['result']['optionList']:
        prd_option_dict = {} # 번역된 옵션이 들어갈 빈 딕셔너리
        for key in prd:
            if (key in option_dict.keys()) == True:
                prd_option_dict[option_dict[key]] = prd[key]
        optionList.append(prd_option_dict)

    return optionList

optionList = make_option_list(data)
pprint.pprint(optionList)

prd_option_list = []
for prd in prd_list:
    prd_option_dict = {}
    prd_option_dict['금리정보'] = []
    for option in optionList:
        prd_option_dict['금융상품명'] = prd['fin_prdt_nm']
        prd_option_dict['금융회사명'] = prd['kor_co_nm']
        if prd['fin_prdt_cd'] == option['금융상품코드']:
            temporary_option = {key: value for key, value in option.items() if key != '금융상품코드'}
            prd_option_dict['금리정보'].append(temporary_option)
    prd_option_list.append(prd_option_dict)

pprint.pprint(prd_option_list)