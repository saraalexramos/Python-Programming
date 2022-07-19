# Use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. 
# The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

def no_shouting(list):
    new_list =[]
    for i in range (len(list)):

        if list[i].isupper():
            continue
        else:
            new_list.append(list[i])
    
    return new_list

if __name__ == "__main__":
    
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
            