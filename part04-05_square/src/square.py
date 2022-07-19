import sys

def line(num, string):
    i = 0

    while i < num:
        if string == "":
            string = "*"

        print(string[0], end = "")
        i += 1

def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1
        sys.stdout.write("\n")


if __name__ == "__main__":
    square(5, "x")