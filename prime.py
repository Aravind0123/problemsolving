for num in range(200,300):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)