# app.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    while True:
        try:
            temp_input = input("Enter the temperature value (or type 'exit' to quit): ")
            if temp_input.lower() == "exit":
                print("Exiting program. Goodbye!")
                break

            temp_value = float(temp_input)
            unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().lower()

            if unit == 'c':
                converted = celsius_to_fahrenheit(temp_value)
                print(f"{temp_value}°C is {converted:.2f}°F\n")
            elif unit == 'f':
                converted = fahrenheit_to_celsius(temp_value)
                print(f"{temp_value}°F is {converted:.2f}°C\n")
            else:
                print("Invalid unit. Please enter 'C' or 'F'.\n")

        except ValueError:
            print("Invalid temperature input. Please enter a numeric value.\n")
