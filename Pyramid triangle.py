rows= int(input("Enter the row:"))
for i in range(0,rows):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(chr(alph),end=" ")
        alph +=1
    alph = 65

    print(" ")
