def palindromes(str1):

    str2 = str1[::-1]
    if str2 == str1:
        print(f"{str1} is a palindrome!")
        return True
    else:
        print("that wasn't a palindrome")
        return False

while False:
    str3 = input("Please type in a palindrome: ")
    palindromes(str3)



if __name__ == "__main__":
    palindromes("dwefvcwv")