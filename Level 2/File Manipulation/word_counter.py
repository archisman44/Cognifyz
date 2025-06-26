from flask import Flask, render_template_string, request, session
import re
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt'}

# Create uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Word Counter</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-color);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      transition: background-color 0.3s, color 0.3s;
    }
    .counter {
      background-color: var(--card-color);
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      width: 400px;
    }
    .counter h2 {
      text-align: center;
      margin-bottom: 1rem;
    }
    .counter input, .counter button {
      width: 100%;
      padding: 0.6rem;
      margin: 0.5rem 0;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 1rem;
    }
    .result {
      margin-top: 1rem;
      font-size: 0.95rem;
      background-color: var(--history-bg);
      border: 1px solid var(--history-border);
      padding: 0.5rem;
      border-radius: 5px;
      max-height: 200px;
      overflow-y: auto;
    }
    .result h4 {
      margin: 0 0 0.5rem;
      font-size: 1rem;
    }
    .result ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .result li {
      padding: 2px 0;
      border-bottom: 1px solid var(--history-border);
    }
    .history {
      margin-top: 1rem;
      font-size: 0.95rem;
      background-color: var(--history-bg);
      border: 1px solid var(--history-border);
      padding: 0.5rem;
      border-radius: 5px;
      max-height: 150px;
      overflow-y: auto;
    }
    .history h4 {
      margin: 0 0 0.5rem;
      font-size: 1rem;
    }
    .history ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .history li {
      padding: 2px 0;
      border-bottom: 1px solid var(--history-border);
    }
    .buttons {
      display: flex;
      justify-content: space-between;
    }
    .buttons button {
      width: 48%;
    }
    .theme-toggle {
      text-align: center;
      margin-top: 1rem;
    }
  </style>
  <script>
    function toggleTheme() {
      const current = localStorage.getItem('theme') || 'light';
      const next = current === 'light' ? 'dark' : 'light';
      localStorage.setItem('theme', next);
      setTheme(next);
    }

    function setTheme(mode) {
      const root = document.documentElement;
      if (mode === 'dark') {
        root.style.setProperty('--bg-color', '#1f2937');
        root.style.setProperty('--text-color', '#f9fafb');
        root.style.setProperty('--card-color', '#374151');
        root.style.setProperty('--accent-color', '#10b981');
        root.style.setProperty('--history-bg', '#4b5563');
        root.style.setProperty('--history-border', '#6b7280');
      } else {
        root.style.setProperty('--bg-color', 'white');
        root.style.setProperty('--text-color', 'black');
        root.style.setProperty('--card-color', '#ffffff');
        root.style.setProperty('--accent-color', '#1f2937');
        root.style.setProperty('--history-bg', '#f9fafb');
        root.style.setProperty('--history-border', '#d1d5db');
      }
    }

    window.onload = () => {
      const savedTheme = localStorage.getItem('theme') || 'light';
      setTheme(savedTheme);
    }
  </script>
  <style>
    :root {
      --bg-color: white;
      --text-color: black;
      --card-color: #ffffff;
      --accent-color: #1f2937;
      --history-bg: #f9fafb;
      --history-border: #d1d5db;
    }
  </style>
</head>
<body>
  <div class="counter">
    <h2>Word Counter</h2>
    <p>Upload a text file to count word occurrences:</p>
    <form method="POST" action="/" enctype="multipart/form-data">
      <input type="file" name="file" accept=".txt" required />
      <div class="buttons">
        <button type="submit">Count Words</button>
      </div>
    </form>
    <div class="buttons" style="margin-top: 0.5rem;">
      <button type="button" onclick="clearHistory()">Clear History</button>
    </div>

    {% if word_counts is not none %}
      <div class="result">
        <h4>Word Counts (Alphabetical Order):</h4>
        <ul>
          {% for word, count in word_counts.items() %}
            <li>{{ word }}: {{ count }}</li>
          {% endfor %}
        </ul>
      </div>
    {% endif %}
    {% if error is not none %}
      <div class="result" style="color: red;">{{ error }}</div>
    {% endif %}

    <div class="history" id="history-container">
      <h4>History:</h4>
      <ul>
        {% for item in history %}
          <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>

    <div class="theme-toggle">
      <button onclick="toggleTheme()">Toggle Theme</button>
    </div>
  </div>

  <script>
    function clearHistory() {
      fetch('/clear', { method: 'POST' })
        .then(response => {
          if (response.ok) {
            document.getElementById('history-container').innerHTML = '<h4>History:</h4><ul></ul>';
          }
        });
    }
  </script>
</body>
</html>
'''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def count_words(file_content):
    # Convert to lowercase and remove punctuation, then split into words
    words = re.findall(r'\b\w+\b', file_content.lower())
    # Count occurrences of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    # Sort alphabetically
    return dict(sorted(word_counts.items()))

@app.route('/', methods=['GET', 'POST'])
def word_counter():
    # Initialize session variables if not present
    if 'history' not in session:
        session['history'] = []

    word_counts = None
    error = None

    if request.method == 'POST':
        if 'file' not in request.files:
            error = "No file part in the request."
            session['history'].append(f"Error: {error}")
        else:
            file = request.files['file']
            if file.filename == '':
                error = "No file selected."
                session['history'].append(f"Error: {error}")
            elif not allowed_file(file.filename):
                error = "Invalid file type. Only .txt files are allowed."
                session['history'].append(f"Error: {error}")
            else:
                try:
                    # Read file content
                    content = file.read().decode('utf-8')
                    word_counts = count_words(content)
                    filename = secure_filename(file.filename)
                    session['history'].append(f"Processed file: {filename} - Total unique words: {len(word_counts)}")
                except Exception as e:
                    error = f"Error processing file: {str(e)}"
                    session['history'].append(f"Error: {error}")

        session.modified = True

    return render_template_string(
        HTML_TEMPLATE,
        word_counts=word_counts,
        error=error,
        history=session['history']
    )

@app.route('/clear', methods=['POST'])
def clear():
    session['history'] = []
    session.modified = True
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)