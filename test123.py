a,b=map(int, input().split())
arr = [0]*6

for i in range(6):
    arr[i] = a
    a += 1

    if(arr[i] > b):
        break
    
    print(arr[i], end='')