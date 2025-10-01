"""
CP1404/CP5632 - Practical
Exceptions Demo
Questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# --- ANSWERS ---
# 1. ValueError occurs when the user inputs something that cannot be converted to int,
#    e.g., letters, symbols, or a blank input.
# 2. ZeroDivisionError occurs when the denominator entered is 0.
# 3. Yes, we can check the denominator before dividing and ask the user to re-enter if it's zero.

# --- SAFER VERSION ---
while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        # Check for zero denominator
        if denominator == 0:
            print("Denominator cannot be zero! Please enter a non-zero number.")
            continue  # ask for input again

        fraction = numerator / denominator
        print(f"Result: {fraction}")
        break  # exit the loop if everything is fine

    except ValueError:
        print("Numerator and denominator must be valid numbers! Please try again.")

print("Finished.")
