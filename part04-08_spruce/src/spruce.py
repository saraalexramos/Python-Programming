
def spruce(num):
    print("a spruce!")
    i = 1
    count = 0
    j = num -1
    while count < num:
        print(" " * j, end = "")
        print("*" * i)
        i += 2
        count +=1
        j -= 1
    i = 1
    j = num -1
    print(" " * j, end = "")
    print("*" * i)


if __name__ == "__main__":
    spruce(5)