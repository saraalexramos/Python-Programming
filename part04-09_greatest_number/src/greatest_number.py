
def greatest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    return num1


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)