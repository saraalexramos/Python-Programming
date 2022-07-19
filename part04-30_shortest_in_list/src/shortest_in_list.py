

def shortest(list):
    lenList = []
    for i in range(len(list)):
        length = len(list[i]) # length of all the strings in the list
        lenList.append(length) # keep the values in a list
        x = min(lenList)
        for i in range(len(lenList)):
            if x == lenList[i]:
                y = i
                break
    return list[y]


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)

