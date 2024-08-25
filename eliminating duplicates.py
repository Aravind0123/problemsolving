str = "Aravind goood apple"
str=str.lower()
new_str = ""
for letter in str:
    if letter not in new_str:
        new_str += letter
print(new_str)
