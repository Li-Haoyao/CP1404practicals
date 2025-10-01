"""
CP1404/CP5632 - Practical
Files practice
"""

# 1. Write user's name to a file using open and close
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Read the name from the file and greet using open and close
in_file = open("name.txt", "r")
name_from_file = in_file.read()  # read the entire content
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read first two numbers from numbers.txt, add them, print result (use with)
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline().strip())
    second_number = int(numbers_file.readline().strip())
    sum_first_two = first_number + second_number
print(sum_first_two)  # Should print 59

# 4. Compute total for all numbers in numbers.txt (use with)
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line.strip())
print(total)  # Prints sum of all numbers in the file
