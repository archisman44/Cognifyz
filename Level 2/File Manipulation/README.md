# Word Counter Web App

# File Manipulation - Cognifyz Level 2 Task 5

## Overview
The Word Counter Web App is a web-based tool built using Flask, a lightweight Python web framework. The app allows users to upload a text file, counts the occurrences of each word in the file, and displays the results in alphabetical order along with their respective counts. The app includes a history tracker and a theme toggle for enhanced user experience. This project was developed as part of a coding challenge (Level 2, Task 5) on June 10, 2025.

## Features
- **Word Counting**: Reads a text file, counts the occurrences of each word, and displays the results in alphabetical order.
- **File Upload**: Supports uploading of `.txt` files via a web form.
- **Input Validation**: Ensures only `.txt` files are processed and handles errors (e.g., invalid file types, empty files).
- **History Tracker**: Keeps a record of processed files and any errors, with an option to clear the history.
- **Theme Toggle**: Switch between light and dark themes, with preferences saved in the browser's local storage.
- **User-Friendly Interface**: Provides a clean interface to upload files, view word counts, and see the history of processed files.

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
   - Alternatively, download the project files (`word_counter.py` and `README.md`) and navigate to the project directory.

2. **Install Dependencies**:
   - Install Flask using pip:
     ```bash
     pip install flask
     ```

3. **Run the Application**:
   - Ensure you have the `word_counter.py` file in your project directory.
   - Run the Flask server:
     ```bash
     python word_counter.py
     ```
   - The app will start on `http://127.0.0.1:5000`. Open this URL in your web browser.

## Usage
1. **Access the Word Counter**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

2. **Upload a Text File**:
   - Click "Choose File" and select a `.txt` file from your computer.
   - Click the "Count Words" button to process the file.
   - The app will display a list of words in alphabetical order along with their counts (e.g., "apple: 3").
   - If there’s an error (e.g., invalid file type), an error message will be shown.

3. **View History**:
   - The history of processed files and errors is displayed below the upload form.
   - Each entry shows the filename and the number of unique words found (or an error message).
   - Click "Clear History" to reset the history.

4. **Toggle Theme**:
   - Click the "Toggle Theme" button to switch between light and dark modes.

## Testing with a Sample File
A sample text file named `test_file.txt` can be used to test the app. Create a file with the following content:

```
The quick brown fox jumps over the lazy dog.
The FOX jumps again! Quick, brown fox, run fast.
Lazy dog sleeps while the quick brown fox JUMPS.
```

### Steps to Test:
1. Save the above content as `test_file.txt` on your computer.
2. Upload `test_file.txt` to the app.
3. The app should display the following word counts in alphabetical order:
   ```
   again: 1
   brown: 3
   dog: 2
   fast: 1
   fox: 3
   jumps: 3
   lazy: 2
   over: 1
   quick: 3
   run: 1
   sleeps: 1
   the: 4
   while: 1
   ```

## File Structure
- `word_counter.py`: The main Flask application file containing the server logic, HTML template, and word counting functionality.
- `README.md`: This file, providing documentation for the project.
- `uploads/`: A directory created automatically to store uploaded files temporarily (though the app reads the file directly and doesn’t save it).

## Example
1. Create a file named `sample.txt` with the following content:
   ```
   Hello world hello Python WORLD python
   ```
2. Upload `sample.txt` to the app.
3. The app will display:
   ```
   hello: 2
   python: 2
   world: 2
   ```

## Screenshots
(You can add screenshots of the word counter interface here if desired, such as the upload form and result display.)

## Known Issues
- The app does not currently support very large files, which may cause performance issues.
- Non-ASCII characters or special encodings in text files may not be handled correctly.

## Future Improvements
- Add support for larger files by processing them in chunks.
- Include a feature to download the word counts as a file (e.g., CSV).
- Enhance the UI with a visual representation of word frequencies (e.g., a bar chart).
- Add support for additional file formats (e.g., `.docx`, `.pdf`).

## Development History
This project was developed as part of a coding challenge (Level 2, Task 5) on June 10, 2025. It builds on the design principles from previous tasks (e.g., Number Guesser, Password Strength Checker, Fibonacci Sequence Generator), including a user-friendly interface, history tracking, and theme toggle.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contact
For any questions or suggestions, please reach out via the project's repository (if applicable) or contact the developer directly.

## 👨‍💻 Author

- **Intern Name:** Archisman Chakraborty  
- **Internship:** Cognifyz Technologies  
- **Level:** 2  
- **Task:** 5 - File Manipulation