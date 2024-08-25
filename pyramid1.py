n=5
a=65
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print(chr(a),end="")
        a+=1
    print()
