string = input("Enter the string: ")
string = string.lower()
new =""
for i in string:
    print(i)
    if i not in new:
        new += i
    if i in new: 
        new.replace(i," ")
print(new)