n=8
for i in range(1,n):
    k=0
    for j in range(i):
        print(k,end='')
        if(k>=1):
            k=0
        else:
            k+=1
    print()