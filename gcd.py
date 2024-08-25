n=int(input("Enter 1st number: "))
m=int(input("Enter 2nd number: "))

gcd=0
if n>m:
    small=m
else:
    small=n
print("GCD are",end=" ")
for i in range(2,small+1):
    if(n%i==0) and (m%i==0):
        print(i,end=" ")