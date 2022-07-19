# A function named anagrams, which takes two strings as arguments. 
# The function returns True if the strings are anagrams of each other. 
# Two words are anagrams if they contain exactly the same characters.

def anagrams(str1, str2):
    str1cpy = sorted(str1)
    str2cpy = sorted(str2)

    if str1cpy == str2cpy:
        return True
    else:
        return False




if __name__ == "__main__":
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False