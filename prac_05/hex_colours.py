"""
Hex Colours
Estimate: 15 minutes
Actual:15
"""

COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blue": "#0000ff",
    "brown": "#a52a2a",
    "coral": "#ff7f50",
    "crimson": "#dc143c",
    "darkgreen": "#006400"
}


def main():
    """Allow user to look up hex colour codes by name."""
    colour_name = input("Enter colour name: ").strip().lower()
    while colour_name != "":
        if colour_name in COLOUR_CODES:
            print(f"{colour_name.title()} is {COLOUR_CODES[colour_name]}")
        else:
            print("Invalid colour name.")
        colour_name = input("Enter colour name: ").strip().lower()


if __name__ == "__main__":
    main()
