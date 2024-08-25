text1 = input("Enter the String1 : ")
text2 = input("Enter the String2 : ")
if(len(text1)!=len(text2)):
    print("Not Anagram")
else:
    if(sorted(text1)==sorted(text2)):
        print("Anagram")
    else:
        print("Not a anagram")