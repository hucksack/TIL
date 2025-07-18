import requests
# url='https://api.agify.io?name=kakarot'
# result=requests.get(url).json()
# print(result)
# print(result['age'])

# print(result.get('age'))
# dic={'이름':'조형준','나이':40}
# # print(dic['주소']) # 에러
# print(dic['이름'])
# print(dic.get('이름'))
# print(dic.get('주소')) 


# # 이름을 입력받기
# # 그리고 입력받은 이름에 해당하는 나이 출력해보기
# # 000의 예상되는 나이는 00세 입니다

# name = input()
# url='https://api.agify.io?name='+name
# result = requests.get(url).json()
# age = result.get('age')

# print(f'{name}의 예상되는 나이는 {age}세 입니다.')


# 확인하고자 하는 로또번호 회차를 입력받기
# MM에 있는 API 활용해서
# 입력받은 회차에 당첨번호만 파싱해서 출력하기 (출력순서 상관 없음)

number = input()
url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+number
result = requests.get(url).json()
# lotto=[]
# # lotto_1 = result.get('drwtNo1')

# # print(lotto_1)

# for i in range(1,7):
#     lotto.append(result.get(f'drwtNo{i}'))

for i in range(1,7):
    words="drwtNo" + str(i)
    print(result.get(words), end=' ')

print(result.get('bnusNo'))

