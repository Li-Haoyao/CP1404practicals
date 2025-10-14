"""
Wimbledon
Estimate: 30 minutes
Actual:30
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions' wins and countries."""
    records = load_data(FILENAME)
    champion_to_wins = count_champions(records)
    countries = extract_countries(records)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read data file and return a list of lists (records)."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() 
        records = [line.strip().split(",") for line in in_file]
    return records


def count_champions(records):
    """Count how many times each champion has won."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def extract_countries(records):
    """Extract a sorted set of countries from the records."""
    countries = {record[1] for record in records}
    return sorted(countries)


def display_results(champion_to_wins, countries):
    """Display champions and number of wins, and list of countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
