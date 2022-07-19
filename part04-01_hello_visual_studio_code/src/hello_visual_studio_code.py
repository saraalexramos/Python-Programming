while True:
    editor = input("Editor: ")
    if editor.lower() == "visual studio code":
        break
    elif editor.lower() == "emacs" or editor.lower() == "vim" or editor.lower() == "atom":
        print("not good")
    elif editor.lower() == "word" or editor.lower() == "notepad":
        print("awful")
print("an excellent choice!")