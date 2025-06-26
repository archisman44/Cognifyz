# Palindrome Checker Web App

# Palindrome Checker Web App - Cognifyz Level 1 Task 5


## Overview
This project is a web-based Palindrome Checker built using Flask, a lightweight Python web framework. It allows users to input a word, phrase, or sequence and check whether it is a palindrome. A palindrome reads the same forward and backward (e.g., "madam", "racecar", or "A man, a plan, a canal: Panama"). The app features a clean user interface with a history tracker and a theme toggle for light and dark modes.

## Features
- **Palindrome Checking**: Determines if a given string is a palindrome, ignoring case, spaces, and special characters.
- **History Tracker**: Keeps track of previous checks, with an option to clear the history.
- **Theme Toggle**: Switch between light and dark themes, with preferences saved in the browser's local storage.
- **Error Handling**: Handles empty or invalid inputs gracefully.

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
   - Ensure you have the `palindrome_app.py` file in your project directory.
   - Run the Flask server:
     ```bash
     python palindrome_app.py
     ```
   - The app will start on `http://127.0.0.1:5000`. Open this URL in your web browser.

## Usage
1. **Access the Palindrome Checker**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

2. **Check a String**:
   - Enter a word, phrase, or sequence in the input field.
   - Click the "Check" button to see if it's a palindrome.
   - The result will display whether the input is a palindrome or not.

3. **View History**:
   - The check history is displayed below the input field.
   - Click "Clear History" to reset the history.

4. **Toggle Theme**:
   - Click the "Toggle Theme" button to switch between light and dark modes.

## File Structure
- `palindrome_app.py`: The main Flask application file containing the server logic, HTML template, and palindrome checker function.
- `README.md`: This file, providing documentation for the project.

## Screenshots
(You can add screenshots of the palindrome checker interface here if desired.)

## Known Issues
- The app does not currently support real-time validation of input as the user types.

## Future Improvements
- Add real-time feedback while typing to indicate if the current input is a palindrome.
- Include additional palindrome-related features, such as finding the longest palindromic substring.
- Enhance the UI with more styling or animations.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact
For any questions or suggestions, please reach out via the project's repository (if applicable) or contact the developer directly.


## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 1  
- **Task:** 5 - Palindrome Checker