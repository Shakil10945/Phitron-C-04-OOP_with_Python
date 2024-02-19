import pyjokes

def tell_some_jokes():
    print("Hello! I'm your joke bot. How many jokes would you like to hear?")
    
    while True:
        try:
            num_jokes = int(input("Enter a number (1-10): "))
            if 1 <= num_jokes <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
    
    for _ in range(num_jokes):
        joke = pyjokes.get_joke()
        print("\nJoke:")
        print(joke)
        # print("\nWould you like to hear another joke? (yes/no)")
        # another_joke = input().strip().lower()
        # if another_joke != 'yes':
        #     break

if __name__ == "__main__":
    tell_some_jokes()
