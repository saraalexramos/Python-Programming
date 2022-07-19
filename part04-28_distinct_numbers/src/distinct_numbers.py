# A function named distinct_numbers, which takes a list of integers as its argument. 
# The function returns a new list containing the numbers from the original list in 
# order of magnitude, and so that each distinct number is present only once.

def distinct_numbers(list):
    list.sort()
    newList = []
    for i in range (len(list)):
        if list[i] in newList:
            continue
        else:
            newList.append(list[i])
    return newList


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))