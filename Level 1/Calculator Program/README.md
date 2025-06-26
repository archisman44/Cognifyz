# Scientific Calculator Web App

# Scientific Calculator Web App - Cognifyz Level 1 Task 4


## Overview
This project is a web-based Scientific Calculator built using Flask, a lightweight Python web framework. It allows users to perform basic arithmetic operations as well as advanced scientific calculations such as trigonometric functions, logarithms, exponentials, factorials, and more. The app features a clean user interface with a history tracker and a theme toggle for light and dark modes.

## Features
- **Basic Operations**: Addition, subtraction, multiplication, division, and modulus.
- **Scientific Functions**: Sine, cosine, tangent, inverse trigonometric functions, logarithms (base 10 and natural), square root, exponential, factorial, absolute value, square, and constants (π, e).
- **Dynamic UI**: Automatically hides the second input field for unary operations (e.g., sin, log, π).
- **Calculation History**: Keeps track of previous calculations, with an option to clear the history.
- **Theme Toggle**: Switch between light and dark themes, with preferences saved in the browser's local storage.
- **Error Handling**: Handles invalid inputs and mathematical errors gracefully (e.g., division by zero, negative logarithms).

## Prerequisites
To run this project, you need the following installed on your system:
- Python 3.6 or higher
- Flask (`pip install flask`)

## Installation
1. **Clone or Download the Project**:
   - If the project is in a repository, clone it:
     ```bash
     git clone <repository-url>
     cd <repository-directory>
     ```
   - Alternatively, download the project files and navigate to the project directory.

2. **Install Dependencies**:
   - Install Flask using pip:
     ```bash
     pip install flask
     ```

3. **Run the Application**:
   - Ensure you have the `app.py` file in your project directory.
   - Run the Flask server:
     ```bash
     python app.py
     ```
   - The app will start on `http://127.0.0.1:5000`. Open this URL in your web browser.

## Usage
1. **Access the Calculator**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

2. **Perform Calculations**:
   - Enter a number in the first input field.
   - Select an operation from the dropdown menu (e.g., `+`, `sin`, `log`).
   - For binary operations (e.g., addition, subtraction), enter a second number.
   - Click the "Calculate" button to see the result.

3. **View History**:
   - The calculation history is displayed below the calculator.
   - Click "Clear History" to reset the history.

4. **Toggle Theme**:
   - Click the "Toggle Theme" button to switch between light and dark modes.

## File Structure
- `app.py`: The main Flask application file containing the server logic, HTML template, and calculation functions.
- `README.md`: This file, providing documentation for the project.

## Screenshots
(You can add screenshots of the calculator interface here if desired.)

## Known Issues
- Memory functions (e.g., MC, MR, M+) are not implemented as they require additional persistent storage.
- The app assumes degree mode for trigonometric functions, as per the initial design.

## Future Improvements
- Add support for memory functions (MC, MR, M+, etc.).
- Implement a toggle for degree/radian modes for trigonometric calculations.
- Add keyboard input support for faster calculations.
- Enhance the UI with a button-based layout similar to a physical calculator.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact
For any questions or suggestions, please reach out via the project's repository (if applicable) or contact the developer directly.

## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 1  
- **Task:** 4 - Calculator Program