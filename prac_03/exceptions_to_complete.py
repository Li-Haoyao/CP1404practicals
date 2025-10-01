"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line -> mark the loop as finished if input is valid
        is_finished = True
    except ValueError:  # TODO - catch the exception when input cannot be converted to int
        print("Please enter a valid integer.")

print("Valid result is:", result)
