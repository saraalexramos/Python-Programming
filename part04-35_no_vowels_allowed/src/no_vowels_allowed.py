# A function named no_vowels, which takes a string argument. 
# The function returns a new string, which should be the same as the original but with all vowels removed.
# Assuming the string will contain only characters from the lowercase English alphabet a...z.


def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    for i in range (len(vowels)):
        string = string.replace(f"{vowels[i]}", "")
    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))