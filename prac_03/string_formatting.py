"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)

Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

# Example variables
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# --- Old style string concatenation (not recommended) ---
# Converts year to string manually and concatenates
print("My guitar: " + name + ", first made in " + str(year))

# --- str.format() examples ---
# Basic replacement fields
print("My guitar: {}, first made in {}".format(name, year))
# Numbered replacement fields
print("My guitar: {0}, first made in {1}".format(name, year))
# Reusing the same field
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# --- f-string formatting (recommended, Python 3.6+) ---
print(f"My {name} was first made in {year} (that's right, {year}!)")

# --- Formatting currency ---
# str.format version with 2 decimal places and comma as thousands separator
print("My {} would cost ${:,.2f}".format(name, cost))
# f-string version (preferred)
print(f"My {name} would cost ${cost:,.2f}")  # {:,.2f} -> comma and 2 decimals

# --- Aligning numbers in columns ---
numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    # {number:5} -> width 5, right-aligned by default
    print(f"Number {i} is {number:5}")

# --- TODO 1: f-string formatting for specified output ---
# Desired output: "1922 Gibson L-5 CES for about $16,036!"
# {:,.0f} -> comma as thousands separator, 0 decimal places (rounds number)
print(f"{year} {name} for about ${cost:,.0f}!")

# --- TODO 2: Right-aligned 2^i table ---
# Range from 0 to 10, right-align both exponent and result
for i in range(11):
    # i:>2 -> exponent right-aligned, width 2
    # 2**i:4 -> result right-aligned, width 4
    print(f"2 ^{i:>2} is {2**i:4}")
