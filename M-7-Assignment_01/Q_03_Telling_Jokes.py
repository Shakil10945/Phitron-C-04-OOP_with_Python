import pyjokes

def tell_some_jokes():
    print("Welcome to the world of jokes")
    while (True):
        try:
            num_joke = int(input("Tell me how many jokes you want to hear: "))
            if 1<=num_joke<=10:
                break
            else:
                print("Enter a valid number: ")
        except ValueError:
            print("Invalid Input")
    for i in range(num_joke):
        print(pyjokes.get_joke())

tell_some_jokes()