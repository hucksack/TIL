lst = [0] * 4

a,b=map(int,input().split())

lst[0] = a
lst[2] = b

for i in range(4):
    print(lst[i], end='')