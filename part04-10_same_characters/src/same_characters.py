
def same_chars(string, x, y):
    if 0 <= x <= (len(string) -1) and 0 <= y <= (len(string) -1):
        if string[x] == string[y]:
            return True
        return False
    return False


if __name__ == "__main__":
    name = same_chars("coder", 1, 2)
    print(name)