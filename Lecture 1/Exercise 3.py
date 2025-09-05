
# Exercise 3: Write a Python function that takes a string as its only argument and prints out the frequency with which each letter occurs in the string. The function should only print out the frequency of occurrence for letters that actually occur in the input string.

def exercise_3(input_string):

    string = input_string
    frequency = {}

    for letter in string:

        if letter.isalpha(): # Uncomment this line to make the function only count letters.
            frequency[letter] = frequency.get(letter, 0) + 1

            # Uncomment the following line to make the function case-insensitive
            # letter = letter.lower()
            # frequency[letter] = frequency.get(letter, 0) + 1

    for letter, count in frequency.items():
        print(f"{letter}: {count}")

input = "Pneumonoultramicroscopicsilicovolcanoconiosis is the longest word in the world!"
exercise_3(input)
