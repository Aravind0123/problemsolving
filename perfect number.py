n=int(input("Enter any number:"))
perfect=0
for i in range(1,n):
    if(n%i==0):
        perfect+=i
if(perfect==n):
    print(n,"It is a Perfect Number")
else:
    print(n,"Is Not a Perfect Number")