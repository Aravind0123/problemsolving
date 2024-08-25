rows = int(input("Enter rows:"))
for i in range(rows):
    for j in range(rows-i):
        print(" ",end=" ")
    m=1
    for k in range(1,2*i):
        print(m,end=" ")
        m+=1
    print(" ")