import sys

def line(num, string):
    i = 0

    while i < num:
        if string == "":
            string = "*"

        print(string[0], end = "")
        i += 1

def shape(num1, string1, num2, string2):
    i = 1
    while i <= num1:
        line(i, string1)
        i += 1
        sys.stdout.write("\n")
    j = 0
    while j < num2:
        line(num1, string2)
        j += 1
        sys.stdout.write("\n")

if __name__ == "__main__":
    shape(5, "x", 2, "o")