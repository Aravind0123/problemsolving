
n=int(input("Enter th number you want to check it is prime or not: "))
for i in range(2,n):
    if(n%i==0):
        print("Not a prime")
        break
    else:
        print("Prime")
        break