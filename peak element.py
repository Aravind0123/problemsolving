num=[0,1,2,1,0] 
def peak(num,n):
    for i in range(n):
        if(num[i]<num[i-1] and num[i]>num[i+1] ):
            return i
    else:
        return -1
n=len(num)
peak=peak(num,n)
print(peak)