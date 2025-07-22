capital = 'A'
test1 = capital.lower()
test2= chr(ord(capital)+32)
print(test2)

# 리스트
lst = [1,2,3,4]
print(type(lst))
print(len(lst))

lst=[1,2,3,4,[5,6,7],8]
print(lst[4][0])
print(lst[-2][-3])

# range 연속되는 숫자 표현할때 사용
print(list(range(3)))
print(list(range(3,6)))
print(list(range(3,8,2)))

# tuple (값을 바꿀수 없는 순서가 있는 자료형)
lst=[1,2,3]
lst[0]=100

tp=(1,2,3)
print(tp[0])
# tp[0] = 100 # 불가능
print(len(tp))
print(tp[-1])
# 여기까지 순서가 있는 자료형

# 순서가 없는 dictionary(빠른속도로 검색가능)
# 형태: key 와 value로 이루어 졌음
di={1:3,2:{4:5},'학':6,'교':[7,8,9]}
print(di)
print(type(di))
print(di[1])
print(di[2][4])
print(di['학'])
print(di['교'][2])

# 값(value)을 바꾸기
di[2]='이번 여름에는 민어탕을 챙겨먹어야지'
print(di)

# key는 원래 안바뀌는데 pop 이용하면 바꿀 수 있다.
di[111]=di.pop(1)
print(di)

# set 자료형 - 중복을 제거할때 사용 && 집하을 표현할 떄
s={1,2,3,4,5,1}
print(s)
print(type(s))

arr = { 12,3,3,2,3,3,3,3,3,3,3,3,23,2,2,2,2,42,21,42,2,22,2,2}
arr = list(set(arr))
print(arr)

s1 = {1,2,3}
s2 = {3,6,9}
# 합집합
print(s1|s2)
# 차집합
print(s1-s2)
# 교집합
print(s1 and s2)

# boolean
a1 = bool('a')
a2 = bool('')
a3 = bool('.')
print(a1,a2,a3)

test= bool('0') # T
test2= bool('0') # F
test3= bool(-2) # T
test4= bool(5) # T

print("-------------------")
a = True
# 논리연산자
b = True
c = True
ad = True

print(a and b)
print(a and c)
print(a or b)

print("-------------------")

print('a'and 'b')
print('' and 'a')
print(0 and 1)

# and연산자 사용했다 앞에 값이 True 이면 어떤값 반환? (앞 or 뒤)
# and연산자 사용했다 앞에 값이 FALSE 이면 어떤값 반환? (앞 or 뒤)

print(1 or 0)
print(0 or -1)
print(-1 or 1)

# or 연산자
# 앞에가 True면 ( 앞? , 뒤? ) 값 반환
# 앞에가 Flase면 ( 앞? , 뒤? ) 값 반환

a=1
b=0
c=3
print('------------------') # 논리연산자
print(a or c) # a 1
print(b or c) # c 3
print(a and b) # b 0
print(a and c) # c 3
print(c and a) # a 1

print('------------------')   # 비트연산자
print(a|c)   # 3
print(b|c)   # 3
print(a&b)   # 0
print(a&c)   # 1
print(c&a)   # 1

print('------------------')

# 연산자 우선순위
result=10 % 3 + 2 ** 2

print(result)

result= -3 ** 2

print(result)

# 객체를 비교하는 is
# 객체의 주소값을 비교하는 연산 : is

a=2
b=2.0

if a==b:
    print('정답')
else:
    print('오답')

if a is b:
    print('정답')
else:
    print('오답')