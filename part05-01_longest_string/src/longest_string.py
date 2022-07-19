# Please write a function named longest(strings: list), which takes a list of strings as its argument. 
# The function finds and returns the longest string in the list. 
# You may assume there is always a single longest string in the list.


def longest(strings: list):
    i = 0

    while i < len(strings): # to run alll the positions in string list
        if i == 0: # in the first iteration of the loop
            longestStr = strings[0] #longestStr (longest String) is equal to the string in first positions in strings
        elif i != 0:
            if len(strings[i]) > len(longestStr):
                longestStr = strings[i]
        i += 1
    
    return longestStr
        


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
