"""
CP1404/CP5632 - Practical
Exploring the random module in Python.
"""

import random

print(random.randint(5, 20))      # line 1
print(random.randrange(3, 10, 2)) # line 2
print(random.uniform(2.5, 5.5))   # line 3
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
