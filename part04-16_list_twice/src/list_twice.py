list1 = []

while True:
    num = int(input("New item: "))
    if num == 0:
        print("Bye!")
        break
    list1.append(num)
    print(f"The list now: {list1}")
    print(f"The list in order: {sorted(list1)}")
