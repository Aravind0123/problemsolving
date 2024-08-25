pos=0
def binary(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid]== n :
            globals() ['pos']=mid
            print(n,"Found at: ", pos)
            break
        else:
            if (list[mid]<n):
                l = mid + 1
            else:
                u= mid - 1
    else:
        print(n,"not found")
        binary(list,int(input("Enter another number : ")))
        
list = [2,3,5,9,77,89]
n = int(input("Enter input: "))
binary(list,n)
        