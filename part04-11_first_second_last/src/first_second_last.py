
def first_word(string):
    str2 = string.split()
    return str2[0]

def second_word(string):
    str2 = string.split()
    return str2[1]

def last_word(string):
    str2 = string.split()
    return str2[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))