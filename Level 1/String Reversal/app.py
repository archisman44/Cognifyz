# app.py

def reverse_string(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    while True:
        user_input = input("Enter a string to reverse (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
        reversed_string = reverse_string(user_input)
        print("Reversed string:", reversed_string)
