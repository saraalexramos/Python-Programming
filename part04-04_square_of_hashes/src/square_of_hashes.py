import sys

def line(num, string):
    i = 0

    while i < num:
        if string == "":
            string = "*"

        print(string[0], end = "")
        i += 1

def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1
        sys.stdout.write("\n")

if __name__ == "__main__":
    square_of_hashes(5)
