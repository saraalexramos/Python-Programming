list = []
i = 1

while True:

    print(f"The list is now {list}")
    letter = input("a(d)d, (r)emove or e(x)it: ")
    
    if letter == "d":
        list.append(i)
        i += 1
    if letter == "r":
        list.pop(-1)
        i -= 1
    if letter == "x":
        print("Bye!")
        break