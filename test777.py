A, B = map(int,input().split())

def output(a,b):
    cnt = 5
    while(cnt <= a+b):
        print(cnt,end=' ')
        cnt += 1

output(A,B)