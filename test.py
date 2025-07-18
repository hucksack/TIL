# 변수 variable 값1개를 저장~
# 리스트 list (배열 array) : 값을 여러개 저장할때 사용

my_list=['java','django','C++','HTML','python']

# 리스트의 원소 접근
print(my_list[0])

# 리스트 안의 값 변경
my_list[0] = 'python'

# 리스트 길이 출력
print(len(my_list))

# 인덱싱
print(my_list[1:4])
print(*(my_list[1:4])) # *을 astrisk or 애스터리스트 or 아스트랄

# 1. 어제 먹은 음식들로 채워진 리스트를 만들어보시오.
y_list = ['족발','보쌈','피자','치킨','떡볶이','냉면']

# 2. 첫번째 음식을 출력하시오.
print(y_list[0])

# 3. 두번째로 먹은 음식을 초밥으로 바꾸세요. 그리고 리스트 전체 출력
y_list[1] = '초밥'
print(*y_list)



# 딕셔너리 (이름 표(key)를 단 여러개의 값을 저장) (키:값)
# 해쉬(hash) 자료구조를 기반을 만들어진 자료형
# key와 value의 형태로 이루어 짐

di={'이름': '조형준', '나이':25, '성별':'남'}
print(di['나이']) 

'''
딕셔너리 실습1
'''

#1-1. 자신의 이름(name), 나이(age), 인사말(msg)로 구성된 my_info 라는
#     dictionary를 만들어 보세요. 그리고 딕셔너리를 출력해주세요

my_di = {'이름' : '조형준', '나이' : 25, '인사말' : '반갑습니다.'}
print(my_di['인사말'])


phone_number={
    '최':'010',
    '민':'9353',
    '호':'6698',
    'studyterm': {'stcamp':'3days',
                 'python':'2weeks',
                 'algorithm': '6weeks'},
    111:'굳굳'}

# 파이썬을 학습하는 기간이 얼마인지 출력해 주세요!!!!

# a = phone_number['studyterm']
# print(a['python'])

print(phone_number['studyterm']['python'])

a = input() # 문자열 입력
b = int(input()) # 정수값 입력
# print(type(a))
lst=[1,2,3,4,5]
lst=list(map(int, input().split()))
print(lst)












