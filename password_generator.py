import random
import string


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Random Password Generator ===")

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            return

        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(
            length,
            uppercase,
            numbers,
            symbols
        )

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()