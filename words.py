while True:
        print("enter 'x' for exit");
        string=input("enter any string\n")
        if string=='x':
            break
        else:
             word_length=len(string.split())
             print("number of words\n")
             print(word_length)
