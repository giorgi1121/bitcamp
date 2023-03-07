#Exercise 1.3
#create main function
def main():
    # create variable with inforamtion about user name
    name = input("What is your name? ")
    # change name into the title version
    name = name.title()
    #call hello function
    print(hello(name))

#create hello function which greetings in different ways
def hello(to):
    if to == "Giorgi":
        return "Hello, giorgi, nice to meet you."
    elif to.startswith("D"):
        return "Hello, " + to + ", how are you?"
    elif to.startswith("O"):
        return "Hi, " + to + ", what\'s up?"
    elif to.startswith("N"):
        return to + ", how you doin?"
    else:
        return "Hi, " + to

main()
