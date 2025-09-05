
# Write a Python function that takes any sequence as its argument and returns the reverse of the sequence. Get the function to notify the user when the input sequence is a palindrome.

def exercise_4(input_sequence):

    sequence = input_sequence

    reversed_sequence = sequence[::-1] # Reverses using slicing by [start:stop:step], so a step of -1 goes backwards from stop to start.

    if str(sequence).lower() == str(reversed_sequence).lower(): # Converts to string and compares without case sensitivity.
        return "Wow! " + str(sequence) + " is a palindrome!"
    else:
        return reversed_sequence

input_sequence = [1, 2, 3, 4, 5]
input_palindrome = "Saippuakivikauppias"

print(exercise_4(input_sequence))
print(exercise_4(input_palindrome))
