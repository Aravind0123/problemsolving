list =[9,88,5,6,5,2,5,1]
no_duplicates = []
for i in list:
    if i not in no_duplicates:
        no_duplicates.append(i)
print(no_duplicates)