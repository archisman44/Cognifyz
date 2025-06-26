# Number Guessing Game Web App

# Number Guessing Game Web App - Cognifyz Level 2 Task 1

## Overview
This project is a web-based Number Guessing Game built using Flask, a lightweight Python web framework. The app generates a random number between 1 and 100, and the user tries to guess it. After each guess, the app provides feedback ("too high" or "too low") until the correct number is guessed or the maximum attempts (6) are reached. The app features a clean user interface with a guess history tracker, a theme toggle for light and dark modes, and options to show the answer, start a new game, or clear the history.

## Features
- **Random Number Generation**: Generates a random number between 1 and 100 for each game.
- **Feedback Mechanism**: Provides "too high" or "too low" hints after each guess.
- **Guess Counter**: Tracks the number of attempts, with a maximum of 6 attempts per game.
- **Show Answer Option**: Allows the user to reveal the answer at any time using the "Show Answer" button.
- **Automatic Answer Reveal**: Automatically reveals the answer after the 6th attempt if the user hasn't guessed correctly.
- **History Tracker**: Keeps a record of all guesses, with options to clear the history or start a new game.
- **Theme Toggle**: Switch between light and dark themes, with preferences saved in the browser's local storage.
- **Error Handling**: Handles invalid inputs (e.g., non-numeric values, numbers outside the range).

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
   - Ensure you have the `guessing_game.py` file in your project directory.
   - Run the Flask server:
     ```bash
     python guessing_game.py
     ```
   - The app will start on `http://127.0.0.1:5000`. Open this URL in your web browser.

## Usage
1. **Access the Number Guessing Game**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

2. **Play the Game**:
   - Enter a number between 1 and 100 in the input field.
   - Click the "Guess" button to submit your guess.
   - The app will provide feedback:
     - "Too high!" if your guess is greater than the target number.
     - "Too low!" if your guess is less than the target number.
     - "Correct!" if you guessed the number, along with the number of attempts taken.
     - After 6 attempts, if you haven't guessed correctly, the answer is revealed, and a new game starts.
   - After a correct guess or revealing the answer, the game automatically starts a new round.

3. **Show the Answer**:
   - Click the "Show Answer" button to reveal the target number at any time. This will end the current game and start a new one.

4. **View History**:
   - The guess history is displayed below the input field.
   - Click "Clear History" to reset the history.

5. **Start a New Game**:
   - Click "New Game" to generate a new random number and reset the guess counter and history.

6. **Toggle Theme**:
   - Click the "Toggle Theme" button to switch between light and dark modes.

## File Structure
- `guessing_game.py`: The main Flask application file containing the server logic, HTML template, and game functionality.
- `README.md`: This file, providing documentation for the project.

## Screenshots
(You can add screenshots of the guessing game interface here if desired.)

## Known Issues
- The app does not currently support real-time validation of input as the user types.

## Future Improvements
- Add a hint system (e.g., "You're close!" when the guess is within 5 of the target).
- Implement a high score system to track the fewest attempts across games.
- Enhance the UI with more styling or animations for feedback.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact
For any questions or suggestions, please reach out via the project's repository (if applicable) or contact the developer directly.


## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 2  
- **Task:** 1 - Guessing Game