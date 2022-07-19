
times = int (input("How many times: "))
i = 1
list1 = []

while i <= times:
    num = int(input(f"Item {i}: "))
    list1.append(num)
    i += 1
print(list1)
