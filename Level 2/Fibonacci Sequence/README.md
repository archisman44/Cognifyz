# Fibonacci Sequence Generator Web App

# Fibonacci Sequence Web App - Cognifyz Level 2 Task 4

## Overview
The Fibonacci Sequence Generator Web App is a web-based tool built using Flask, a lightweight Python web framework. The app allows users to input a number of terms and generates the Fibonacci sequence up to that number of terms. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones (e.g., 0, 1, 1, 2, 3, 5, ...). The app includes a history tracker and a theme toggle for enhanced user experience. This project was developed as part of a coding challenge (Level 2, Task 4) on June 10, 2025.

## Features
- **Fibonacci Sequence Generation**: Generates the Fibonacci sequence up to a user-specified number of terms.
- **Input Validation**: Ensures the input is a positive integer, displaying an error message for invalid inputs.
- **History Tracker**: Keeps a record of generated sequences and any errors, with an option to clear the history.
- **Theme Toggle**: Switch between light and dark themes, with preferences saved in the browser's local storage.
- **User-Friendly Interface**: Provides a clean and simple interface to input the number of terms and view the resulting sequence.

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
   - Alternatively, download the project files (`fibonacci_sequence.py` and `README.md`) and navigate to the project directory.

2. **Install Dependencies**:
   - Install Flask using pip:
     ```bash
     pip install flask
     ```

3. **Run the Application**:
   - Ensure you have the `fibonacci_sequence.py` file in your project directory.
   - Run the Flask server:
     ```bash
     python fibonacci_sequence.py
     ```
   - The app will start on `http://127.0.0.1:5000`. Open this URL in your web browser.

## Usage
1. **Access the Fibonacci Sequence Generator**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

2. **Generate a Fibonacci Sequence**:
   - Enter the number of terms (e.g., 5) in the input field.
   - Click the "Generate Sequence" button.
   - The app will display the Fibonacci sequence (e.g., for 5 terms: [0, 1, 1, 2, 3]).
   - If the input is invalid (e.g., negative number or non-integer), an error message will be shown.

3. **View History**:
   - The history of generated sequences and errors is displayed below the input field.
   - Click "Clear History" to reset the history.

4. **Toggle Theme**:
   - Click the "Toggle Theme" button to switch between light and dark modes.

## File Structure
- `fibonacci_sequence.py`: The main Flask application file containing the server logic, HTML template, and Fibonacci sequence generation functionality.
- `README.md`: This file, providing documentation for the project.

## Screenshots
(You can add screenshots of the Fibonacci sequence generator interface here if desired, such as the input form and result display.)

## Known Issues
- The app does not currently support real-time validation of input as the user types (e.g., preventing non-numeric input before submission).
- Very large numbers of terms (e.g., >100) may result in large sequences that could affect performance or display.

## Future Improvements
- Add real-time input validation to prevent invalid submissions.
- Include a visual representation of the Fibonacci sequence (e.g., a chart or spiral).
- Optimize the sequence generation for large numbers of terms.
- Add a feature to download the sequence as a file.

## Development History
This project was developed as part of a coding challenge (Level 2, Task 4) on June 10, 2025. It builds on the design principles from previous tasks (e.g., Number Guesser, Password Strength Checker), including a user-friendly interface, history tracking, and theme toggle.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact
For any questions or suggestions, please reach out via the project's repository (if applicable) or contact the developer directly.

## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 2  
- **Task:** 4 - Fibonacci Sequence