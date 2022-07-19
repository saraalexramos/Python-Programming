# A function named everything_reversed, which takes a list of strings as its argument. 
# The function returns a new list with all of the items on the original list reversed. 
# Also the order of items should be reversed on the new list


def everything_reversed(list):
    list2 = []
    for i in range (len(list)): 
        word = list[i]
        wordf = word[::-1]
        list2.append(wordf)
    
    list2 = list2[::-1]

    return list2


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)