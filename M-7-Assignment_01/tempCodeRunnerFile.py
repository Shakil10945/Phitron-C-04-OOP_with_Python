def create_new_string():
    # List of words to be matched
    a = ['oh', 'Emelia', 'to']

    # Input string
    s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

    # Convert input string to lowercase for case-insensitive matching
    s_lower = s.lower()

    # Split the input string into words
    words = s_lower.split()

    # Initialize an empty list to store matched words
    matched_words = []

    # Iterate through the words and check for matches
    for word in words:
        if word in a:
            # If the word is in the list 'a', add the next word to the matched list
            index = words.index(word)
            if index + 1 < len(words):
                matched_words.append(words[index + 1])

    # Create the output string by joining the matched words
    output_string = ' '.join(matched_words)

    # Write the output string to the file 'out.txt'
    with open('out.txt', 'w') as file:
        file.write(output_string)

# Call the function to execute the task
create_new_string()
