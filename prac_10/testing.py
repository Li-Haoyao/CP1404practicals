"""
CP1404/CP5632 Practical 10 - Testing
"""

import doctest
from prac_06.car import Car  # Make sure you have this module

# -----------------------------
# repeat_string function
# -----------------------------
def repeat_string(s, n):
    """Repeat string s, n times, separated by spaces."""
    return " ".join([s] * n)

# -----------------------------
# is_long_word function
# -----------------------------
def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

# -----------------------------
# format_phrase_as_sentence function
# -----------------------------
def format_phrase_as_sentence(phrase):
    """
    Format phrase as a sentence: capitalize first letter, end with period.
    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_as_sentence("python is fun")
    'Python is fun.'
    """
    sentence = phrase.strip()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence[0].upper() + sentence[1:]

# -----------------------------
# test function
# -----------------------------
def run_tests():
    """Run assert tests."""
    # repeat_string tests
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"
    # Car tests
    car_default = Car()
    assert car_default._odometer == 0, "Car does not set odometer correctly"
    assert car_default.fuel == 0, "Car does not set default fuel correctly"
    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set fuel when provided"
    print("All assert tests passed!")

# -----------------------------
# main program
# -----------------------------
if __name__ == "__main__":
    run_tests()
    doctest.testmod()
