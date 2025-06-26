# Number Guesser Web App

# Number Guesser Web App - Cognifyz Level 2 Task 2

## Overview
The Number Guesser Web App is a web-based game built using Flask, a lightweight Python web framework. The app challenges users to guess a randomly generated number within a user-specified range, providing feedback ("too high" or "too low") after each guess. The game is designed with a clean and minimal initial interface, strict gameplay rules (e.g., a 6-attempt limit), and user-friendly features like a history tracker and theme toggle. This project was developed as part of a coding challenge (Level 2, Task 2) and has been iteratively improved based on user feedback.

## Features
- **Minimal Initial Interface**: On first load, the app only displays a "Set Range" form to specify the number range, ensuring a focused start to the game.
- **Custom Range**: Users can define the minimum and maximum values for the number range (e.g., 10 to 50).
- **Random Number Generation**: Generates a random number within the user-specified range for each game.
- **Feedback Mechanism**: Provides "too high" or "too low" hints after each guess to guide the user.
- **Strict 6-Attempt Limit**: Users are limited to exactly 6 attempts per game. After the 6th attempt, the answer is revealed, and no further guesses are allowed until the user starts a new game.
- **Show Answer Option**: Users can reveal the answer at any time using the "Show Answer" button, ending the current game.
- **Manual Game Restart**: After the game ends (correct guess, 6 attempts, or showing the answer), the user must manually click "New Game" to restart and set a new range.
- **History Tracker**: Keeps a record of all guesses, with an option to clear the history.
- **Theme Toggle**: Switch between light and dark themes, with preferences saved in the browser's local storage.
- **Error Handling**: Handles invalid inputs (e.g., non-numeric values, invalid ranges) with appropriate error messages.

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
   - Alternatively, download the project files (`number_guesser.py` and `README.md`) and navigate to the project directory.

2. **Install Dependencies**:
   - Install Flask using pip:
     ```bash
     pip install flask
     ```

3. **Run the Application**:
   - Ensure you have the `number_guesser.py` file in your project directory.
   - Run the Flask server:
     ```bash
     python number_guesser.py
     ```
   - The app will start on `http://127.0.0.1:5000`. Open this URL in your web browser.

## Usage
1. **Access the Number Guesser**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

2. **Set the Range**:
   - On the initial screen, you’ll see only the "Set Range" form.
   - Enter the minimum and maximum values for the range (e.g., Min: 10, Max: 50).
   - Click "Set Range" to start the game.

3. **Play the Game**:
   - Once the range is set, the full interface appears.
   - Enter a number within the specified range.
   - Click the "Guess" button to submit your guess.
   - The app will provide feedback:
     - "Too high!" if your guess is greater than the target number.
     - "Too low!" if your guess is less than the target number.
     - "Correct!" if you guessed the number, along with the number of attempts taken.
     - After exactly 6 attempts, if you haven't guessed correctly, the answer is revealed, and the game ends.
   - The attempt counter displays "Attempts: X/6" to show your progress.
   - Once the game ends (correct guess, 6 attempts, or showing the answer), the guessing interface is replaced with a "New Game" button.

4. **Show the Answer**:
   - Click the "Show Answer" button to reveal the target number at any time. This will end the current game and display the answer.

5. **View History**:
   - The guess history is displayed below the input field once the range is set.
   - Click "Clear History" to reset the history without restarting the game.

6. **Start a New Game**:
   - Click "New Game" to return to the "Set Range" screen and start a new game.

7. **Toggle Theme**:
   - Click the "Toggle Theme" button (available after setting the range) to switch between light and dark modes.

## File Structure
- `number_guesser.py`: The main Flask application file containing the server logic, HTML template, and game functionality.
- `README.md`: This file, providing documentation for the project.

## Screenshots
(You can add screenshots of the number guesser interface here if desired, such as the initial "Set Range" screen and the gameplay interface.)

## Known Issues
- The app does not currently support real-time validation of input as the user types (e.g., preventing non-numeric input before submission).
- The "Guess" button is disabled after 6 attempts, but users might still try to interact with the form if they don’t notice the disabled state.

## Future Improvements
- Add a hint system (e.g., "You're close!" when the guess is within a certain range of the target).
- Implement a high score system to track the fewest attempts across games.
- Enhance the UI with animations for feedback (e.g., a shake effect for incorrect guesses).
- Add real-time input validation to prevent invalid submissions.

## Development History
This project was developed as part of a coding challenge (Level 2, Task 2) on June 10, 2025. The following updates were made based on user feedback:
- **Initial Version**: Created a number guessing game with a fixed range (1-100), a "Show Answer" button, and automatic answer reveal after 6 attempts.
- **Custom Range**: Added the ability for users to specify a custom range for the number to guess.
- **Manual Restart**: Modified the app to show the answer after 6 attempts without automatically restarting, requiring the user to click "New Game".
- **Minimal Initial Interface**: Updated the app to show only the "Set Range" form on initial load, with the full interface appearing after the range is set.
- **Strict 6-Attempt Limit**: Ensured the app enforces exactly 6 attempts, disabling the guess input after the limit is reached and clarifying the attempt count in the UI.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact
For any questions or suggestions, please reach out via the project's repository (if applicable) or contact the developer directly.

## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 2  
- **Task:** 2 - Number Guesser