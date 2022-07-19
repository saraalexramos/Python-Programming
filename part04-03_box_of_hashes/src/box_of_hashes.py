import sys

def line(num, string):
    i = 0

    while i < num:
        if string == "":
            string = "*"

        print(string[0], end = "")
        i += 1

def box_of_hashes(height):
    i = 0
    while i < height:
        line(10, "#")
        i += 1
        sys.stdout.write("\n") # to change the line without print function

if __name__ == "__main__":
    box_of_hashes(5)
