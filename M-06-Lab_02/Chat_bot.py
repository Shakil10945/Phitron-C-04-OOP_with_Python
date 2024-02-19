def listen():
    return input("Say Something: ")

def decide(command):
    command = command.lower()
    broken_words = command.split(" ")
    for word in broken_words:
        if word in greet_words:
            talkback("Hi Man, Hoow are you")
            break
        elif word in bye_words:
            talkback("Tata bye bye byee. see you soon")
            break
        elif word in bad_words:
            talkback("Dustumi koro na")
            break
def talkback(response):
    print(response)

greet_words = ['hi', 'hello', 'yo', 'hey']
bye_words = ['bye', 'tata', 'hasta la vista']
bad_words = ['dog', 'pocha', 'kutta']

print("Welcome to the cahtbot")

while True:
    anymore = input("Do you want to chat with me? YES/ NO : ")
    if anymore.lower()=='no':
        print("thanks for your time")
        break
    command =listen()
    decide(command)
