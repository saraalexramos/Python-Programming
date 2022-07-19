
list1 = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i == -1:
        break
    value = int(input("New value: "))
    list1[i] = value
    print(list1)