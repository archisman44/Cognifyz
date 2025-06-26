import re

def is_valid_email(email):
    # Check for double dots
    if '..' in email:
        return False

    # Use a stricter pattern that avoids consecutive special characters and checks domain
    pattern = r"(^[a-zA-Z0-9]+[._-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$"

    # Match against the pattern
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    print("📧 Email Validator Program (type 'exit' to quit)\n")
    while True:
        user_input = input("Enter an email address: ")
        if user_input.lower() == 'exit':
            print("👋 Exiting...")
            break
        if is_valid_email(user_input):
            print(f"✅ '{user_input}' is a valid email address.\n")
        else:
            print(f"❌ '{user_input}' is NOT a valid email address.\n")
