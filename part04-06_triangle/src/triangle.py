import sys

def line(num, string):
    i = 0

    while i < num:
        if string == "":
            string = "*"

        print(string[0], end = "")
        i += 1

def triangle(size):
    i = 1
    while i <= size:
        line( i, "#")
        i += 1
        sys.stdout.write("\n")


if __name__ == "__main__":
    triangle(5)
