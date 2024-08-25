
for i in range(1,500):
    perfect=0
    for j in range(1,i):
        if(i%j==0):
            perfect=perfect+j
    if(perfect==i):
        print(perfect)
