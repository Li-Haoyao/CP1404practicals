MIN_LENGTH = 5

def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    """Prompt user for a valid password."""
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long")
        password = input("Enter password: ")
    return password

def print_asterisks(password, symbol="*"):
    """Print asterisks (or other symbol) the same length as the password."""
    print(symbol * len(password))

main()