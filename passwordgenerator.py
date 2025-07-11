import random
import string

def generate_password(length: int) -> str:
    """
    Generates a random password with letters, digits, and special characters.
    Ensures at least one character of each type is included.
    """
    if length < 4:
        return "Password should be at least 4 characters long!"

    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation + "@"

    
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

   
    random.shuffle(password)

    return ''.join(password)

def main():
    user_input = input("Enter desired password length: ").strip()

    if not user_input.isdigit() or int(user_input) <= 0:
        print(" Please enter a valid positive number.")
        return

    length = int(user_input)
    pwd = generate_password(length)
    print(f"\n🔐 Generated Password ({length} chars):\n{pwd}\n")

if __name__ == "__main__":
    main()
