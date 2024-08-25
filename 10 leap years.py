count=0
for i in range(2000,2050):
    if(i%4==0 and i%100!=0) or (i%400==0):
        count=count + 1
        if(count<=10):
            print(i)
        else:
            break