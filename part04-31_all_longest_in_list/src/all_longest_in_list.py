# Please write a function named all_the_longest, which takes a list of strings as its argument. 
# The function should return a new list containing the longest string in the original list. 
# If more than one are equally long, the function should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.


def all_the_longest (list):
    lenList = []
    spot_in_list = []
    new_list = []

    for i in range (len(list)):
        length = len(list[i]) # length of all the strings in the list
        lenList.append(length) # keep the values in lenList
        
    x = max(lenList) # maximum length of the strings

    for i in range(len(lenList)):
        if x == lenList[i]: # find the position of the longest strings
            spot_in_list.append(i) # and keep the information in spot_in_list
        else:
            continue
    
    for i in range(len(spot_in_list)):
        new_list.append(list[spot_in_list[i]])
    
    return new_list


if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']