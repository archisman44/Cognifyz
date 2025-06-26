from flask import Flask, render_template_string, request, session
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Number Guessing Game</title>
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
    .game {
      background-color: var(--card-color);
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      width: 350px;
    }
    .game h2 {
      text-align: center;
      margin-bottom: 1rem;
    }
    .game input, .game button {
      width: 100%;
      padding: 0.6rem;
      margin: 0.5rem 0;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 1rem;
    }
    .result {
      margin-top: 1rem;
      text-align: center;
      font-weight: bold;
      font-size: 1.2rem;
      color: var(--accent-color);
    }
    .history {
      margin-top: 1rem;
      font-size: 0.95rem;
      background-color: var(--history-bg);
      border: 1px solid var(--history-border);
      padding: 0.5rem;
      border-radius: 5px;
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
  <div class="game">
    <h2>Number Guessing Game</h2>
    <p>Guess a number between 1 and 100 (Attempts: {{ guess_count }}):</p>
    <form method="POST" action="/">
      <input type="number" name="guess" min="1" max="100" placeholder="Enter your guess" required />
      <div class="buttons">
        <button type="submit">Guess</button>
      </div>
    </form>
    <div class="buttons" style="margin-top: 0.5rem;">
      <button type="button" onclick="showAnswer()">Show Answer</button>
      <button type="button" onclick="restartGame()">New Game</button>
    </div>
    <div class="buttons" style="margin-top: 0.5rem;">
      <button type="button" onclick="clearHistory()">Clear History</button>
    </div>

    {% if feedback is not none %}
      <div class="result">{{ feedback }}</div>
    {% endif %}

    <div class="history" id="history-container">
      <h4>Guess History:</h4>
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
            document.getElementById('history-container').innerHTML = '<h4>Guess History:</h4><ul></ul>';
          }
        });
    }

    function restartGame() {
      fetch('/restart', { method: 'POST' })
        .then(response => {
          if (response.ok) {
            window.location.reload();
          }
        });
    }

    function showAnswer() {
      fetch('/show_answer', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
          alert("The answer is: " + data.answer);
          restartGame();
        });
    }
  </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def guessing_game():
    # Initialize session variables if not present
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
    if 'history' not in session:
        session['history'] = []
    if 'guess_count' not in session:
        session['guess_count'] = 0

    feedback = None

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['guess_count'] += 1

            if guess < 1 or guess > 100:
                feedback = "Please guess a number between 1 and 100."
                session['history'].append(f"Guess {guess}: Invalid (out of range)")
            elif guess == session['target_number']:
                feedback = f"Correct! You guessed the number in {session['guess_count']} attempts."
                session['history'].append(f"Guess {guess}: Correct! (Attempts: {session['guess_count']})")
                session['target_number'] = random.randint(1, 100)
                session['guess_count'] = 0
            elif session['guess_count'] >= 6:
                feedback = f"Game Over! The answer was {session['target_number']}."
                session['history'].append(f"Game Over after 6 attempts: The answer was {session['target_number']}")
                session['target_number'] = random.randint(1, 100)
                session['guess_count'] = 0
            elif guess < session['target_number']:
                feedback = "Too low!"
                session['history'].append(f"Guess {guess}: Too low")
            else:
                feedback = "Too high!"
                session['history'].append(f"Guess {guess}: Too high")

        except ValueError:
            feedback = "Please enter a valid number."
            session['history'].append("Invalid input: Not a number")

    return render_template_string(HTML_TEMPLATE, feedback=feedback, history=session['history'], guess_count=session['guess_count'])

@app.route('/clear', methods=['POST'])
def clear():
    session['history'] = []
    return ('', 204)

@app.route('/restart', methods=['POST'])
def restart():
    session['target_number'] = random.randint(1, 100)
    session['guess_count'] = 0
    session['history'] = []
    return ('', 204)

@app.route('/show_answer', methods=['POST'])
def show_answer():
    answer = session['target_number']
    return {'answer': answer}

if __name__ == '__main__':
    app.run(debug=True)