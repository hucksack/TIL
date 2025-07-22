# 변수
a=3
b=5 # 값을 넣는다 할당한다 초기화한다 하드코딩하세요
a,b=3,5 # 각각 동시에 할당 가능
print(a+b)

# swap (값 교환하기 - 바꾼다)
# 방법 1
temp=b
b=a
a=temp
print(a,b)

# 방법 2
y,x=1,5
y,x=x,y
print(y,x)

# boolean - 0-거짓 0이외의 숫자-참
a,b=0,-1
a,b=bool(a),bool(b)
print(a,b)

a='3' # 문자열(문장)
# print(a+3) # 에러
# print(int(a) + 3) # 6
print(type(a))

# 소수점!!!
a = 3.14
print(type(a))
print(round(a,1)) # 소수 첫번째 까지 출력(둘째자리에서 반올림)
print(f'소수점 첫번째 자리까지 f-string으로 출력 {a:.1f}')

a = 3.15
print(round(a,1)) # 3.1

# 파이썬이 소수점을 처리할때 정확한 계산이 불가능
# 컴퓨터는 이진수 0과 1로 모든 수를 표현하는데
# 그러다 보니 컴퓨터가 이진수가지고 모든 소수점을 표현하는데 어려움 발생
# 실수를 표현하고 계산하기 위한 다양한 연구가 진행되었는데
# 파이썬에서는 부동소수점 이라는 것을 이용해서 실수를 표현한다.

# 부동소수점으로 실수를 표현할때 정확한 표현이 불가능해서 근사값으로 표현을 함
# 정확한 값이 아니라 근사값으로 표현을 하다보니 그 과정중에 정확하게
# 출력이 안되는 경우가 있다. < floating point error >

a =1.2-1.1
print(a) # 0.09999999999999987
print(round(a,1))

# alt+shift+down = 코드복사
print(round(0.4))
print(round(1.4))
print(round(2.4))
print(round(3.4))
print(round(4.4))
print(round(5.4))

print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))

# 파이썬에서 반올림을 할때 round 내장함수를 이용한다고 했다.
# 하지만 소수를 반올림해서 정수값으로 표현할 때
# 파이썬 그리고 JS (Javascript)에서는 사사오입이 아니라 오사오입 을 사용한다
# 오사오입이란? 5이하는 내림 그리고 5초과는 올림 처리

# 그리고 수점 첫째 자리가 5일 경우에는
# 앞자리가 홀수면 올림 짝수면 내림처리 해버린다.

print(round(0.15, 1))
print(round(0.25, 1))
print(round(0.35, 1))
print(round(0.45, 1 ))
print(round(0.55, 1))

# 파이썬에서 반올림처리해서 출력할때 우리의 의도대로 출력안됨!!
# 이유 1. 파이썬에서는 오사오입을 적용
# 이유 2. 소수점을 오사오입하는 과정중, 소수점 처리를 근사값으로 하다 보니
#         계산과정에서 오류 발생
# 지금까지 결론: 파이썬에서 round함수 쓴다고 모든 값이 반올림을 정상적으로 처리 못함


# 해결책: 소수점을 정확하게 계산할수 있도록 임이의 아주 작은수를 더해서 round 처리하면
#        우리의 의도대로 출력 가능
print(round(0.05, 1)) # 아주 작은 값 더하지 않고 그냥 round 사용했을 경우
print(round(0.15,1))
print(round(0.25,1))
print(round(0.35,1))
print(round(0.45,1))


print(round(0.05+0.000001,1))
print(round(0.15+0.000001,1))
print(round(0.25+0.000001,1))
print(round(0.35+0.000001,1))
print(round(0.45+0.000001,1))
print(round(0.55+0.000001,1))
print(round(0.55+1e-8,1)) # 0.000000001 을 더한 꼴


value = 21e8 # 지수표기법 - 21곱하기 10의 8승 : 21억

# 기억해야 할것!
# 파이썬 소숫점 정확히 표현 못함 (floating point error 떄문)
# 그래서 임이의 작은수를 더해서 계산해야 한다.
# 반올림 round 함수를 사용할 때 반드시 작은수를 더한 다음에 사용하시오 !

# 시퀀스 ( 순서 라는 개념이 있는 자료형 ) -  string list tuple range
s="abcdefg"
print(s[1],s[-6])
# 슬라이싱
print(s[:3]) # 3번인덱스 전까지 (abc)
print(s[3:]) # 3번 인덱스 부터 끝까지 (defg)
print(s[2:5]) # 2번 부터 5번 전까지(4번까지) (cde)
print(s[5:2:-1]) # 5번부터 2번보다 클때까지 1씩 감소 (fed)
print(s[1:6:2]) # 1번부터 5번까지 2번증가 (bdf)
print(s[::-1]) # gfedcba

# 문자열 연산
# print('3' + 3)
print('3' + '55555')
print('3' * 5)

# 문자열은 인덱스로 접근 가능
s="abcdefg"
print(s[1])

# 리스트
lst=[1,2,3,4,5]
lst[1]=222
print(lst) # [1, 222, 3, 4, 5]

# s="abcdefg"
# s[1]='h' # 불가능
# print(s)

# 문자열을 인덱스로 접근은 가능하나 값은 못바꿈
ret = s.replace(s[1], 'h')
print(ret)

capital='A'
test1=capital.lower()
print(test1)