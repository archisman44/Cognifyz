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
  <title>Number Guesser</title>
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
    .game input:disabled, .game button:disabled {
      background-color: #e5e7eb;
      cursor: not-allowed;
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
    .range-inputs {
      display: flex;
      gap: 0.5rem;
    }
    .range-inputs input {
      width: 48%;
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
    <h2>Number Guesser</h2>
    {% if not range_set %}
      <p>Enter the range for the number to guess:</p>
      <form method="POST" action="/set_range">
        <div class="range-inputs">
          <input type="number" name="min_value" placeholder="Min" required />
          <input type="number" name="max_value" placeholder="Max" required />
        </div>
        <div class="buttons">
          <button type="submit">Set Range</button>
        </div>
      </form>
    {% else %}
      {% if game_over %}
        <p>Game Over! The answer was {{ target_number }}.</p>
        <div class="buttons">
          <button type="button" onclick="restartGame()">New Game</button>
        </div>
      {% else %}
        <p>Guess a number between {{ min_value }} and {{ max_value }} (Attempts: {{ guess_count }}/6):</p>
        <form method="POST" action="/">
          <input type="number" name="guess" min="{{ min_value }}" max="{{ max_value }}" placeholder="Enter your guess" required {{ 'disabled' if guess_count >= 6 else '' }} />
          <div class="buttons">
            <button type="submit" {{ 'disabled' if guess_count >= 6 else '' }}>Guess</button>
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
    {% endif %}
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
            window.location.href = '/'; // Force full page reload
          }
        })
        .catch(error => {
          console.error('Error restarting game:', error);
          window.location.href = '/'; // Fallback to full reload
        });
    }

    function showAnswer() {
      fetch('/show_answer', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
          alert("The answer is: " + data.answer);
          window.location.reload(); // Reload to reflect game_over state
        });
    }
  </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def guessing_game():
    # Initialize session variables if not present
    if 'range_set' not in session:
        session['range_set'] = False
        session['min_value'] = 0
        session['max_value'] = 0
        session['target_number'] = 0
        session['history'] = []
        session['guess_count'] = 0
        session['game_over'] = False

    feedback = None

    if not session['range_set']:
        return render_template_string(HTML_TEMPLATE, range_set=False)

    if session['game_over']:
        return render_template_string(
            HTML_TEMPLATE,
            range_set=True,
            min_value=session['min_value'],
            max_value=session['max_value'],
            target_number=session['target_number'],
            history=session['history'],
            guess_count=session['guess_count'],
            game_over=True
        )

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['guess_count'] += 1

            if guess < session['min_value'] or guess > session['max_value']:
                feedback = f"Please guess a number between {session['min_value']} and {session['max_value']}."
                session['history'].append(f"Guess {guess}: Invalid (out of range)")
            elif guess == session['target_number']:
                feedback = f"Correct! You guessed the number in {session['guess_count']} attempts."
                session['history'].append(f"Guess {guess}: Correct! (Attempts: {session['guess_count']})")
                session['game_over'] = True
            elif session['guess_count'] >= 6:
                feedback = f"Game Over! The answer was {session['target_number']}."
                session['history'].append(f"Game Over after 6 attempts: The answer was {session['target_number']}")
                session['game_over'] = True
            elif guess < session['target_number']:
                feedback = "Too low!"
                session['history'].append(f"Guess {guess}: Too low")
            else:
                feedback = "Too high!"
                session['history'].append(f"Guess {guess}: Too high")

        except ValueError:
            feedback = "Please enter a valid number."
            session['history'].append("Invalid input: Not a number")

    return render_template_string(
        HTML_TEMPLATE,
        range_set=session['range_set'],
        min_value=session['min_value'],
        max_value=session['max_value'],
        feedback=feedback,
        history=session['history'],
        guess_count=session['guess_count'],
        game_over=session['game_over']
    )

@app.route('/set_range', methods=['POST'])
def set_range():
    try:
        min_value = int(request.form['min_value'])
        max_value = int(request.form['max_value'])

        if min_value >= max_value:
            session['history'].append("Error: Minimum value must be less than maximum value.")
            return render_template_string(HTML_TEMPLATE, range_set=False)

        session['min_value'] = min_value
        session['max_value'] = max_value
        session['target_number'] = random.randint(min_value, max_value)
        session['guess_count'] = 0
        session['history'] = []
        session['range_set'] = True
        session['game_over'] = False

    except ValueError:
        session['history'].append("Error: Please enter valid numbers for the range.")
        return render_template_string(HTML_TEMPLATE, range_set=False)

    return render_template_string(
        HTML_TEMPLATE,
        range_set=True,
        min_value=session['min_value'],
        max_value=session['max_value'],
        feedback=None,
        history=session['history'],
        guess_count=session['guess_count'],
        game_over=False
    )

@app.route('/clear', methods=['POST'])
def clear():
    session['history'] = []
    return ('', 204)

@app.route('/restart', methods=['POST'])
def restart():
    session['range_set'] = False
    session['min_value'] = 0
    session['max_value'] = 0
    session['target_number'] = 0
    session['guess_count'] = 0
    session['history'] = []
    session['game_over'] = False
    session.modified = True
    return ('', 204)

@app.route('/show_answer', methods=['POST'])
def show_answer():
    answer = session['target_number']
    session['game_over'] = True
    session.modified = True
    return {'answer': answer}

if __name__ == '__main__':
    app.run(debug=True)