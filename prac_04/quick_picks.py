"""
CP1404/CP5632 Practical
Quick Picks lottery ticket generator
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    quick_picks_count = int(input("How many quick picks? "))
    for _ in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate one quick pick (list of sorted unique random numbers)."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:  # avoid duplicates
            numbers.append(number)
    numbers.sort()
    return numbers


main()
