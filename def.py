# # 함수 - 자주 사용할 코드들을 묶어 놓은 형태

# # 사용자 정의함수
# # rabbit 함수를 정의 한다

# def rabbit():
#     print('   ()   ()   ')

# rabbit() # 호출한다

# # 내장함수
# lst = [1,2,3,4]
# print(len(lst))


# def getSum(a,b):     # 매개변수 (parameter) 파라메타
#     print(a+b)
#     print('#')

# getSum(3,7)         # 인자값 / argument 야규먼트
# print("*****")


# def getSum2(a,b):
#     print(a+b)
#     return
#     print('@@@@@@@@')
#     # result = a+b
#     # return result

# ret=getSum2(3,7)
# print(ret)


# ------------------------------------------

# def getNum(y,x):
#     pass
#     return y+x, y*x
#     print("#")

# result = getNum(3,6)
# print("#")
# print(result)
# print(type(result))

# ------------------------------------------

# def getSum(a,b,c=3,d=4):            # 디폴트 파라메타는 무적권 맨 뒤에다가 써야함
#     return a+b+c+d

# getSum(1,2)


# num = [1,2,3,4] # 패킹
# num = (1,2,3,4)

# a,b,c,d = num # 언패킹
# print(a,b,c,d)

# num = [1, 2, 3, 4, 5, 6, 7, 8]
# a,b, *c=num
# print(a,b,c) # 1 2 [3, 4, 5, 6, 7, 8]

# a, *b, c =num
# print(a,b,c) # 1 [2, 3, 4, 5, 6, 7] 8

 
# def getsum_3(*a):                       # 가변 인자
#     print(type(a)) # <class 'tuple'>
#     return a[0]+a[1]+a[2]

# ret = getsum_3(1,2,3,4) 
# print(ret)

# ------------------------------------------

# # 키워드 가변 인자

# def print_info(**args):  # asterisk 아스트랄 (*을 의미)
#     print(args)
#     print(type(args)) # <class 'dict'>


# print_info(kevin=1,john=2,bob=3) # {'kevin': 1, 'john': 2, 'bob': 3}

# di={'kevin' : 1, 'john' : 2, 'bob' : 3}

# def print_info2(ppp):
#     for i,j in ppp.items(): # kevin 3 john 2 bob 3
#         print(i,j, end=' ')

# print_info2(di) # {'kevin': 1, 'john': 2, 'bob': 3}


# ------------------------------------------

# 변수의 범위 scope
# 변수를 사용하면서 변수를 사용할 때 변수의 종류가 2가지 = 지역변수 / 전역변수


# def abc():
#     aa=3
#     bb=5
#     print(aa,bb)
# abc()
# print(aa,bb)
