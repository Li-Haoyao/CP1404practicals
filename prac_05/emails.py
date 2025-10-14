"""
Emails
Estimate: 25 minutes
Actual:25
"""

def main():
    """Store emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from the given email address."""
    name_part = email.split("@")[0]
    parts = name_part.replace(".", " ").split()
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()
