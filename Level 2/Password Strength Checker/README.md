# Password Strength Checker Web App

# Password Strength Checker Web App - Cognifyz Level 2 Task 3

## Overview
The Password Strength Checker Web App is a web-based tool built using Flask, a lightweight Python web framework. The app allows users to enter a password and evaluates its strength based on criteria such as length, presence of uppercase and lowercase letters, digits, and special characters. The app provides detailed feedback on the password's strength and keeps a history of checked passwords. This project was developed as part of a coding challenge (Level 2, Task 3) on June 10, 2025.

## Features
- **Password Strength Evaluation**: Evaluates passwords based on the following criteria:
  - **Length**: At least 8 characters for "moderate", 12 or more for "strong".
  - **Uppercase Letters**: At least one uppercase letter (A-Z).
  - **Lowercase Letters**: At least one lowercase letter (a-z).
  - **Digits**: At least one digit (0-9).
  - **Special Characters**: At least one special character (e.g., !@#$%^&*).
- **Strength Levels**:
  - **Weak**: Fails to meet at least 2 criteria.
  - **Moderate**: Meets most criteria (at least 4 out of 5).
  - **Strong**: Meets all criteria and has a length of 12 or more characters.
- **Detailed Feedback**: Displays specific details about the password (e.g., length, presence of uppercase letters).
- **History Tracker**: Keeps a record of checked passwords (masked for privacy) with their strength levels, with an option to clear the history.
- **Theme Toggle**: Switch between light and dark themes, with preferences saved in the browser's local storage.
- **Privacy**: Passwords in the history are masked (e.g., "P****d" for "Password") to protect user privacy.

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
   - Alternatively, download the project files (`password_checker.py` and `README.md`) and navigate to the project directory.

2. **Install Dependencies**:
   - Install Flask using pip:
     ```bash
     pip install flask
     ```

3. **Run the Application**:
   - Ensure you have the `password_checker.py` file in your project directory.
   - Run the Flask server:
     ```bash
     python password_checker.py
     ```
   - The app will start on `http://127.0.0.1:5000`. Open this URL in your web browser.

## Usage
1. **Access the Password Strength Checker**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

2. **Check a Password**:
   - Enter a password in the input field.
   - Click the "Check Strength" button to evaluate the password.
   - The app will display:
     - The strength level ("Weak", "Moderate", or "Strong").
     - Detailed feedback on the password (e.g., "Length: 8; Uppercase letters: Yes; ...").

3. **View History**:
   - The history of checked passwords is displayed below the input field.
   - Passwords are masked for privacy (e.g., "P****d" for "Password").
   - Click "Clear History" to reset the history.

4. **Toggle Theme**:
   - Click the "Toggle Theme" button to switch between light and dark modes.

## File Structure
- `password_checker.py`: The main Flask application file containing the server logic, HTML template, and password strength checking functionality.
- `README.md`: This file, providing documentation for the project.

## Screenshots
(You can add screenshots of the password strength checker interface here if desired, such as the input form and result display.)

## Known Issues
- The app does not currently support real-time validation of input as the user types (e.g., showing strength while typing).
- The list of special characters is limited to common ones; additional special characters could be included.

## Future Improvements
- Add real-time password strength feedback as the user types.
- Include a password generator feature to suggest strong passwords.
- Enhance the UI with visual indicators (e.g., a strength bar or color-coded feedback).
- Expand the list of special characters for more comprehensive checking.

## Development History
This project was developed as part of a coding challenge (Level 2, Task 3) on June 10, 2025. It builds on the design principles from previous tasks (e.g., Number Guesser), including a user-friendly interface, history tracking, and theme toggle.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact
For any questions or suggestions, please reach out via the project's repository (if applicable) or contact the developer directly.

## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 2  
- **Task:** 3 - Password Strength Checker