# A function named most_common_character, which takes a string argument. 
# The function returns the character which has the most occurrences within the string. 
# If there are many characters with equally many occurrences, the one which appears first in the string should be returned.


def most_common_character(string):
    list1 = []
    for i in string:
        x = string.count(i)
        list1.append(x)
    maxi = max(list1)


    for i in range(len(list1)):
        if maxi == list1[i]:
            y = i
            break
        
    
    return string[y]

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))