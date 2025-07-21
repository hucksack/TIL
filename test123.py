a,b = input().split()

for i in range(4):
    for j in range(ord(a),ord(b)+1):
        print(chr(j),end=' ')
    print()