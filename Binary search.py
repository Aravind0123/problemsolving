list =[2,3,5,9,11,12]
n=int(input("Enter the Number: "))
pos=0
def binary(list,n):
    l=0
    u=len(list)-1
    while l<=u :
        mid = (l+u)//2
        if(list[mid]==n):
            globals()['pos']=mid
            print(n,"Found at:",pos)
            break
        else:
            if(list[mid]<n):
                l=mid +1 
            else:
                u=mid-1
    else:
        print("Not found",n)
        binary(list,int(input("enter another number:")))
            
binary(list,n)
            
            