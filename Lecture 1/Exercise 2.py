
# Exercise 2: Write a Python function that takes a list of numbers as input and outputs the maximum, minimum and median values in the list.

def exercise_2(input_numbers):

    numbers = input_numbers

    # numbers.sort() # Uncomment this line to sort the numbers

    return max(numbers), min(numbers), numbers[len(numbers)//2]

input = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(exercise_2(input))