str1 = input("Please type in string 1: ")
str2 = input("Please type in string 2: ")

if len (str1) == len (str2):
    print("The strings are equally long")
if len (str1) > len (str2):
    print(f"{str1} is longer")
if len (str1) < len (str2):
    print(f"{str2} is longer")
