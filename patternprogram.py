str = "program"
n=len(str)
m=(int)(n/2)
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(m,m+i):
        if(k>=n):
            k=k-n
            print(str[k],end="")
        else:
            print(str[k],end="")
    print(" ")