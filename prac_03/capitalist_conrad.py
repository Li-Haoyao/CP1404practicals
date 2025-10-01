"""
CP1404/CP5632 - Practical
Capitalist Conrad - Stock Price Simulator
Updated version:
- Tracks number of days
- Customizable constants (price range, max increase/decrease)
- Writes output to a file
"""

import random

# --- CONSTANTS ---
FILENAME = "capitalist_conrad_output.txt"
MAX_INCREASE = 0.175  # 17.5% max daily increase
MAX_DECREASE = 0.05   # 5% max daily decrease
MIN_PRICE = 1.0       # minimum price allowed
MAX_PRICE = 100.0     # maximum price allowed
INITIAL_PRICE = 10.0  # starting price

# --- INITIAL SETTINGS ---
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Print starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

# --- SIMULATION LOOP ---
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    # Determine if price increases or decreases (50% chance)
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)  # increase
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)  # decrease

    # Update price
    price *= (1 + price_change)

    # Print current day and price
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()

print(f"Simulation complete. Output written to {FILENAME}")
